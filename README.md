# Wu Tang Financial
personal finance labeling &amp; overview tool

### How to use

This application is built to use ING Bank Netherlands bank statements in CSV format, or any CSV that follows the same format. 

##### Obtain the input file
If you are an ING Online Banking user, click 'download' at any account overview, select 'CSV' as output format, and dowload it.

##### Load input in application
Rename the CSV file to finance_records.csv and replace the file in the test_input folder with this one.


#### Example input

| Datum    | Naam / Omschrijving   | Rekening  | Tegenrekening | Code | Af Bij | Bedrag (EUR)   | MutatieSoort       | Mededelingen          |
|----------|-----------------------|-----------|---------------|------|--------|----------------|--------------------|-----------------------|
| 20180629 | Phone company         | MY123     | XX123         | IC   | Af     | 33,50          | Incasso            | Phone bill 23-06-2018 |
| 20180628 | Myself                | MY123     |               | OV   | Af     | 500,00         | Overschrijving     | To savings account    |
| 20180622 | My Employer           | MY123     | XX123         | OV   | Bij    | 3000,00        | Overschrijving     | Salaris juni 2018     |
| 20180610 | Irish pub Molly's     | XX123     |               | BA   | Af     | 55,00          | Betaalautomaat     | Pasvolgnr:007         |
| 20180605 | Super Market          | XX123     |               | BA   | Af     | 53,50          | Betaalautomaat     | Pasvolgnr:007         |
| 20180605 | Texaco                | XX123     |               | BA   | Af     | 52,10          | Betaalautomaat     | Pasvolgnr:007         |
| 20180603 | Super Market          | XX123     |               | BA   | Af     | 34,65          | Betaalautomaat     | Pasvolgnr:007         |
| 20180503 | Water company         | MY123     | XX123         | IC   | Af     | 20,50          | Incasso            | Water bill            |
| 20180603 | Super Market          | XX123     |               | BA   | Af     | 33,10          | Betaalautomaat     | Pasvolgnr:007         |
| 20180602 | Car insurance company | MY123     | XX123         | IC   | Af     | 33,50          | Incasso            | Car insurance         |
| 20180601 | My Friend             | MY123     | XX123         | GT   | Af     | 7,00           | Online bankieren   | Netflix               |
| 20180601 | Real Estate Rentals   | MY123     | XX123         | IC   | Af     | 1020,50        | Incasso            | Rent june 2018        |

#### Example output

```
-------------------------
June 2018
-------------------------
2018-06-29 Q2 -33.50 utilities Phone company - Phone bill 23-06-2018
2018-06-28 Q2 -500.00 saving Myself - To savings account
2018-06-22 Q2 3000.00 salary My Employer - Salaris juni 2018
2018-06-10 Q2 -55.00 leisure Irish pub Molly's - Pasvolgnr:007
2018-06-03 Q2 -34.65 groceries Super Market - Pasvolgnr:007
2018-06-05 Q2 -53.50 groceries Super Market - Pasvolgnr:007
2018-06-05 Q2 -52.10 automotive Texaco - Pasvolgnr:007
2018-06-03 Q2 -33.10 groceries Super Market - Pasvolgnr:007
2018-06-02 Q2 -33.50 automotive Car insurance company - Car insurance
2018-06-01 Q2 -7.00 subscriptions My Friend - Netflix
2018-06-01 Q2 -1020.50 accomodation Real Estate Rentals - Rent june 2018
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
