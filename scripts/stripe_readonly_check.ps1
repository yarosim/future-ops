# Read-only Stripe revenue check (no writes)
$apiKey = $env:STRIPE_API_KEY; if (-not $apiKey) { throw "Missing STRIPE_API_KEY env" }
$hdr = @{ Authorization = "Basic " + [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(($key + ":"))) }
$fmt = { param($u) [DateTimeOffset]::FromUnixTimeSeconds($u).ToString('yyyy-MM-dd HH:mm') }

"--- CHECKOUT SESSIONS (recent 20) ---"
(Invoke-RestMethod -Uri "https://api.stripe.com/v1/checkout/sessions?limit=20" -Headers $hdr).data | ForEach-Object {
  "{0} UTC | {1} | {2} | {3}" -f (& $fmt $_.created), $_.payment_status, ($_.amount_total/100), $_.customer_details.email
}

"--- SUBSCRIPTIONS ACTIVE ---"
(Invoke-RestMethod -Uri "https://api.stripe.com/v1/subscriptions?status=active&limit=10" -Headers $hdr).data | ForEach-Object { "$($_.id) $($_.status)" }

$since = [DateTimeOffset]::new(2026,9,6,12,0,0,[TimeSpan]::Zero).ToUnixTimeSeconds()
"--- CHARGES since 2026-09-06 ---"
(Invoke-RestMethod -Uri "https://api.stripe.com/v1/charges?created%5Bgt%5D=$since&limit=20" -Headers $hdr).data | ForEach-Object {
  "{0} UTC | {1} | {2} | {3}" -f (& $fmt $_.created), $_.status, ($_.amount/100), $_.description
}

"--- PAYOUTS (last 5) ---"
(Invoke-RestMethod -Uri "https://api.stripe.com/v1/payouts?limit=5" -Headers $hdr).data | ForEach-Object {
  "{0} UTC | {1} | {2}" -f (& $fmt $_.created), $_.status, ($_.amount/100)
}
