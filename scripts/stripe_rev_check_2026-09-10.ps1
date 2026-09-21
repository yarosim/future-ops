$ErrorActionPreference = 'Stop'
# Load key silently from legacy file (read-only use; do not print)
$apiKey = $env:STRIPE_API_KEY; if (-not $apiKey) { throw "Missing STRIPE_API_KEY env" }
$hdr = @{ Authorization = "Bearer $key" }

function Q($path) { Invoke-RestMethod -Uri "https://api.stripe.com/v1/$path" -Headers $hdr }

$cutoff = [DateTimeOffset]::new(2026,8,11,0,0,0,[TimeSpan]::Zero).ToUnixTimeSeconds()
$charges = (Q "charges?limit=100&created[gte]=$cutoff")
Write-Output "=== CHARGES SINCE 2026-08-11: $($charges.data.Count) ==="
foreach ($c in $charges.data) {
  Write-Output ("{0} | {1} | {2} | {3} | created {4}" -f $c.id, $c.status, $c.paid, ($c.amount/100), ([DateTimeOffset]::FromUnixTimeSeconds($c.created).ToString('u')))
}
$all = (Q "charges?limit=3")
Write-Output "=== LATEST 3 CHARGES (any date) ==="
foreach ($c in $all.data) {
  Write-Output ("{0} | {1} | {2} | {3} | created {4}" -f $c.id, $c.status, $c.paid, ($c.amount/100), ([DateTimeOffset]::FromUnixTimeSeconds($c.created).ToString('u')))
}
Write-Output "=== CHECKOUT SESSIONS (latest 10) ==="
$sess = (Q "checkout/sessions?limit=10")
foreach ($s in $sess.data) {
  Write-Output ("{0} | status={1} | payment={2} | {3} | created {4}" -f $s.id, $s.status, $s.payment_status, ($s.amount_total/100), ([DateTimeOffset]::FromUnixTimeSeconds($s.created).ToString('u')))
}
Write-Output "=== CUSTOMERS (latest 5) ==="
$cust = (Q "customers?limit=5")
foreach ($cu in $cust.data) {
  Write-Output ("{0} | {1} | created {2}" -f $cu.id, $cu.email, ([DateTimeOffset]::FromUnixTimeSeconds($cu.created).ToString('u')))
}
Write-Output "=== BALANCE ==="
(Q "balance") | ConvertTo-Json -Depth 4
Write-Output "=== PAYOUTS (latest 5) ==="
$pay = (Q "payouts?limit=5")
foreach ($p in $pay.data) {
  Write-Output ("{0} | {1} | {2} | arrival {3}" -f $p.id, $p.status, ($p.amount/100), ([DateTimeOffset]::FromUnixTimeSeconds($p.arrival_date).ToString('u')))
}
