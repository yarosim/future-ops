$ErrorActionPreference = "Stop"
$env = @{}
Get-Content "$env:USERPROFILE\.openclaw\credentials\stripe.env" | ForEach-Object {
  if ($_ -match "^(STRIPE_API_KEY|STRIPE_WEBHOOK_SECRET)=(.*)$") { $env[$matches[1]] = $matches[2].Trim() }
}
$sk = $env["STRIPE_API_KEY"]
if (-not $sk) { throw "no key" }

function Get-Stripe($path) {
  $r = curl.exe -s -u "$sk`:" "https://api.stripe.com/v1/$path" -H "Stripe-Version: 2024-06-20"
  return $r | Out-String
}

$p1 = "price_1TQG5eEJtdifHfsdKpZBUHps"  # Gap Analysis $299
$p2 = "price_1TQG5gEJtdifHfsd7OAiA42l"  # Managed Compliance $997/mo

Write-Output "=== PAYMENT INTENTS (last 30) ==="
$pi = Get-Stripe "payment_intents?limit=30"
try { $pi | ConvertFrom-Json | Select-Object -Expand data | ForEach-Object {
  $amt = ($_.amount/100)
  $cur = $_.currency
  $stat = $_.status
  $cname = if($_.customer) { $_.customer } else { "(anonymous)" }
  $created = (Get-Date "1970-01-01Z").AddSeconds($_.created).ToString("yyyy-MM-dd HH:mm")
  Write-Output ("{0} | {1} | {2} {3} | {4} | {5}" -f $created, $stat, $amt, $cur, $cname, $_.id)
}} catch { Write-Output $pi }

Write-Output ""
Write-Output "=== CHECKOUT SESSIONS (last 15) ==="
$co = Get-Stripe "checkout/sessions?limit=15"
try { $co | ConvertFrom-Json | Select-Object -Expand data | ForEach-Object {
  $created = (Get-Date "1970-01-01Z").AddSeconds($_.created).ToString("yyyy-MM-dd HH:mm")
  $amt = if($_.amount_total){$_.amount_total/100}else{0}
  Write-Output ("{0} | {1} | status={2} | paid={3} | {4} {5} | {6}" -f $created, $_.id, $_.status, $_.payment_status, $amt, $_.currency, $_.customer_email)
}} catch { Write-Output $co }

Write( "")
Write-Output "=== BALANCE ==="
try { $b = (Get-Stripe "balance" | ConvertFrom-Json); $b.available | ForEach-Object { Write-Output ("available: {0} {1}" -f ($_.amount/100), $_.currency) }; $b.pending | ForEach-Object { Write-Output ("pending: {0} {1}" -f ($_.amount/100), $_.currency) } } catch { "n/a" }

Write( "")
Write-Output "=== PAYOUTS (last 8) ==="
try { Get-Stripe "payouts?limit=8" | ConvertFrom-Json | Select-Object -Expand data | ForEach-Object {
  $created = (Get-Date "1970-01-01Z").AddSeconds($_.created).ToString("yyyy-MM-dd HH:mm")
  Write-Output ("{0} | {1} | {2} {3} | {4}" -f $created, $_.status, ($_.amount/100), $_.currency, $_.arrival_date)
}} catch { "n/a" }