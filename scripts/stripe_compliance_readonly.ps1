$apiKey = $env:STRIPE_API_KEY; if (-not $apiKey) { throw "Missing STRIPE_API_KEY env" }
$creds = $apiKey + ":"
$b64 = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes($creds))
$h = @{ Authorization = "Basic $b64" }
function Get-J($u){ try { Invoke-RestMethod -Uri $u -Headers $h -ErrorAction Stop } catch { return "ERR" } }

Write-Host "=== BALANCE ==="
$bal = Get-J "https://api.stripe.com/v1/balance"
if($bal -ne "ERR"){ "available: $($bal.available[0].amount/100) $($bal.available[0].currency)"; "pending: $($bal.pending[0].amount/100) $($bal.pending[0].currency)" }

Write-Host "`n=== PAYOUTS ==="
$po = Get-J "https://api.stripe.com/v1/payouts?limit=10"
if($po -ne "ERR"){ "count: $($po.data.Count)"; $po.data | ForEach-Object { "$($_.amount/100) $($_.currency) $($_.status) $([DateTimeOffset]::FromUnixTimeSeconds($_.created).DateTime)" } }

Write-Host "`n=== SUBSCRIPTIONS (active) ==="
$sub = Get-J "https://api.stripe.com/v1/subscriptions?status=active&limit=100"
if($sub -ne "ERR"){ "active: $($sub.data.Count)" }

Write-Host "`n=== CUSTOMERS ==="
$cu = Get-J "https://api.stripe.com/v1/customers?limit=100"
if($cu -ne "ERR"){ "total: $($cu.data.Count)"; $cu.data | Select-Object -First 10 | ForEach-Object { "$($_.name) $($_.email) created $([DateTimeOffset]::FromUnixTimeSeconds($_.created).DateTime.ToString('yyyy-MM-dd'))" } }

Write-Host "`n=== CHECKOUT SESSIONS ==="
$cs = Get-J "https://api.stripe.com/v1/checkout/sessions?limit=100"
if($cs -ne "ERR"){ $cs.data | ForEach-Object { "$($_.payment_status) $($_.amount_total/100) $($_.currency) $([DateTimeOffset]::FromUnixTimeSeconds($_.created).DateTime.ToString('yyyy-MM-dd'))" } }

Write-Host "`n=== COMPLIANCE PRICE CHECK ==="
foreach($p in @("price_1TQG5eEJtdifHfsdKpZBUHps","price_1TQG5gEJtdifHfsd7OAiA42l")){
  $r = Get-J "https://api.stripe.com/v1/prices/$p"
  if($r -eq "ERR"){ "$p : NOT FOUND in this account" } else { "$p : product=$($r.product) amount=$($r.unit_amount/100) $($r.currency)" }
}
