# Wu Tang Financial
personal finance labeling &amp; overview tool


##### Example input

| "Datum"    | "Naam / Omschrijving"   | "Rekening" | "Tegenrekening" | "Code" | "Af Bij" | "Bedrag (EUR)"   | "MutatieSoort"       | "Mededelingen"          | 
|------------|-------------------------|------------|-----------------|--------|----------|------------------|----------------------|-------------------------| 
| "20180629" | "Phone company"         | "MY123"    | "XX123"         | "IC"   | "Af"     | "33,50"          | "Incasso"            | "Phone bill 23-06-2018" | 
| "20180628" | "Myself"                | "MY123","" | "OV"            | "Af"   | "500,00" | "Overschrijving" | "To savings account" |                         | 
| "20180622" | "My Employer"           | "MY123"    | "XX123"         | "OV"   | "Bij"    | "3000,00"        | "Overschrijving"     | "Salaris juni 2018"     | 
| "20180610" | "Irish pub Molly's"     | "XX123","" | "BA"            | "Af"   | "55,00"  | "Betaalautomaat" | "Pasvolgnr:007"      |                         | 
| "20180603" | "Super Market"          | "XX123","" | "BA"            | "Af"   | "34,65"  | "Betaalautomaat" | "Pasvolgnr:007"      |                         | 
| "20180605" | "Super Market"          | "XX123","" | "BA"            | "Af"   | "53,50"  | "Betaalautomaat" | "Pasvolgnr:007"      |                         | 
| "20180605" | "Texaco"                | "XX123","" | "BA"            | "Af"   | "52,10"  | "Betaalautomaat" | "Pasvolgnr:007"      |                         | 
| "20180503" | "Water company"         | "MY123"    | "XX123"         | "IC"   | "Af"     | "20,50"          | "Incasso"            | "Water bill"            | 
| "20180603" | "Super Market"          | "XX123","" | "BA"            | "Af"   | "33,10"  | "Betaalautomaat" | "Pasvolgnr:007"      |                         | 
| "20180602" | "Car insurance company" | "MY123"    | "XX123"         | "IC"   | "Af"     | "33,50"          | "Incasso"            | "Car insurance"         | 
| "20180601" | "My Friend"             | "MY123"    | "XX123"         | "GT"   | "Af"     | "7,00"           | "Online bankieren"   | "Netflix"               | 
| "20180601" | "Real Estate Rentals"   | "MY123"    | "XX123"         | "IC"   | "Af"     | "1020,50"        | "Incasso"            | "Rent june 2018"        | 


##### Example output

```
-------------------------
June 2018
-------------------------
date: 2018-06-29 Q2 amount: -33.50 category: utilities << descr: Phone company Phone bill 23-06-2018 >>
date: 2018-06-28 Q2 amount: -500.00 category: saving << descr: Myself To savings account >>
date: 2018-06-22 Q2 amount: 3000.00 category: salary << descr: My Employer Salaris juni 2018 >>
date: 2018-06-10 Q2 amount: -55.00 category: leisure << descr: Irish pub Molly's Pasvolgnr:007 >>
date: 2018-06-03 Q2 amount: -34.65 category: groceries << descr: Super Market Pasvolgnr:007 >>
date: 2018-06-05 Q2 amount: -53.50 category: groceries << descr: Super Market Pasvolgnr:007 >>
date: 2018-06-05 Q2 amount: -52.10 category: automotive << descr: Texaco Pasvolgnr:007 >>
date: 2018-06-03 Q2 amount: -33.10 category: groceries << descr: Super Market Pasvolgnr:007 >>
date: 2018-06-02 Q2 amount: -33.50 category: automotive << descr: Car insurance company Car insurance >>
date: 2018-06-01 Q2 amount: -7.00 category: subscriptions << descr: My Friend Netflix >>
date: 2018-06-01 Q2 amount: -1020.50 category: accomodation << descr: Real Estate Rentals Rent june 2018 >>
-------------------------
total in: 3000.00 total out: -1822.85 end total: 1177.15
-------------------------
salary : 3000.00
accomodation : -1020.50
groceries : -121.25
automotive : -85.60
saving : -500.00
subscriptions : -7.00
utilities : -33.50
leisure : -55.00
```
