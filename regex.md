## 1.1a Vilka strängar matchas av det reguljära uttrycket: "ab" ? Testa era svar på https://regex101.com/ 
- "a b"
- "aBBa"
- "sabotör"

### Answer:
- "sabotör"


## 1.1b Betrakta uttrycket "nisse". Vad skriver jag för att matcha både "Nisse", "NISSE" och "nisse"?

### Answer:
- (?i)nisse

## 1.1c Vilka strängar matchas av "a*n" ?
- "an"
- "amerikan"
- "naturlig"
- "annandag"

### Answer:
- alla

## 1.1d Vilka strängar matchas av "[ae]n" ?
- "naiv"
- "inconsequential"
- "bae"

### Answer:
- "inconsequential"

## 1.1e Vilka strängar matchas av "je.+e"?
- "je"
- "jee"
- "jeppe"
- "je je"

### Answer:
- "jeppe"
- "je je"

## 1.1f Vilka strängar matchas av "\san?\s"
- "sansad"
- " annan "
- "    an   na   an   "
- "be a darling"

### Answer:
The search string reads like this:
> 1 space character, followed by 1 "a" character, followed by 0 or 1 "n" characters, followed by 1 space character
- "    an   na   an   "
- "be a darling"

## 1.1e Skriv ner med egna ord, vad följande uttryck matchar. "Strängar som innehåller…"
- ```"lines?"```
    - match the word line, followed by 0 or 1 "s" characters.
- ```"^a*ö$```
    - Starting from the beginning of the string, match 0 or unlimited "a" characters, followed by a single "ö" character which must be the last character in the string.
- ```"[aeiouyåäö]+"```
    - Match any of the characters a,e,i,o,u,y,å,ä,ö between 1 and unlimited times
- ```"[123456789]\d*"```
    - Match any number from 1,2,3,4,5,6,7,8,9, followed by any digit (between 0 and 9) zero to unlimited times. I.e. any integer that does not begin with zero
- ```"\d{4}-\d{2}-\d{2}"```
    - Match 4 digits (0-9), followed by a single "-" character, followed by 2 digits, followed by a single "-" character, followed by 2 digits. I.e. a number with the format: nnnn-nn-nn


## 2.1a Skriv ett regex som kontrollerar att det finns en längd i strängen, som anges i centimeter:
"Fiskarna som jag fångade var 55 cm långa."

### Answer
```
\d+\s?cm
```

## 2.1b Denna gången vill vi veta om det finns två längder.
"Fiskarna som jag fångade var 55 cm långa. Förre gången fångade jag en som var 62cm lång."

### Answer
``` python
import re

pattern = r"\d+\s?cm"
string = "Fiskarna som jag fångade var 55 cm långa. Förre gången fångade jag en som var 62cm lång."
matches = re.findall(pattern,string)
count = len(matches)

if count == 2:
    print("There are 2 matches")
else:
    print(f"There are not 2 matches. Match count = {count}")
```

## 2.1c Längderna ska vara samma enhet.

### Answer
``` python
import re

pattern = r"\d+\s?c?m"
string = "Fiskarna som jag fångade var 55 cm långa, så båda fick plats i min 1,23 m långa låda."
matches = re.findall(pattern,string)

# set the pattern for extracting the unit
unit_pattern = "c?m"
mismatch = False

for match_idx in range(len(matches)):
    
    unit_match = re.search(unit_pattern, matches[match_idx])
    unit = unit_match[0]
    print(unit)
    if match_idx == 0:
        previous_unit = unit

    else:
        if unit != previous_unit:
            mismatch=True
            break


if mismatch:
    print("Measurement units do not match ❌")
else:
    print("Measurement units are the same ✅")
```





## 2.2 Skriv ett regex som matchar ett svenskt postnummer. Postnummer består av fem siffror indelade i två grupper med mellanslag emellan. Exempel: "123 45"
Om du vill övertänka fördjupa dig mera: https://sv.wikipedia.org/wiki/Postnummer_i_Sverige 

### Answer
```
^\d{3}\s\d{2}$
```

## 2.3 Skriv ett regex som matchar ett datum skrivet enligt den internationella standarden ISO 8601, alltså 10 tecken med bindestreck mellan avdelningarna. Exempel: 2025-03-10.

### Answer

#### Basic pattern match
```
^\d{4}-\d{2}-\d{2}$
```
This simply checks for any 4 digits, followed by "-", then any 2 digits, another "-" and finally 2 digits.


#### More advanced validation
```
^(19|20)\d{2}-(0[123456789]|1[012])-(0[123456789]|1\d|2\d|3[01])
```
This version: 
- limits the date to this century, or the previous century
- only allows for a value between 01 and 12 for the month
- only allows for a day value between 01 and 31
Limitation:
- it does not check validate the day number against the month, e.g. it will accept February 30th (2026-02-30)


#### Test Values
```
2026-04-27
2026/04/27
20260427
26/4/27
26-4-27
2026.04.27
1999-04-27
1999-14-27
1999-94-27
1999-00-27
1999-04-27
1999-04-00
1999-04-29
1999-04-30
1999-04-31
1999-04-32
2022-27-04
2026-02-30
```

## 2.4 Skriv ett regex som matchar ett pengavärde i siffror. Exempel på värden som ska matchas:
200 kr
12,50 kr
0,35 kr

### Answer
```
^\d+(,\d{2})?\s?kr$
```

This checks for: 
- any number of digits at the start of the string
- an optional "," followed by 2 digits (representing öre)
- an optional space " "
- the string "kr" at the end of the string



#### Test values
```
200 kr
12,50 kr
0,35 kr
200, 300 kr
12, 50 kr
12,500 kr
```


## 2.5a Skriv ett regex som matchar en e-postadress (användarnamn@server.domän) enligt följande icke kompletta regler.
- användarnamn kan innehålla bokstäver, siffror och specialtecknen som punkt och bindestreck
- server kan innehålla samma sorts tecken
- domän kan innehålla bokstäver och siffror

### Answer
```
^\S+@\S+\.\S+$
```
This regex pattern looks for:
- any number of non-whitespace characters at the start of the string
- followed by an "@"
- followed by any number of non-whitespace characters
- followed by a "." 
- followewd by any number of non-whitespace characters
 

## 2.5b Gör ett regex som matchar en komplett e-postadress enligt specifikationen i artikeln här:
What is a valid email address format: https://snov.io/knowledgebase/what-is-a-valid-email-address-format/

### Answer
```  
(?i)^[a-z\d]([a-z\d]|[._-](?![._-]))*@[a-z\d]([a-z\d]|[._-](?![._-]))*(\.[a-z\d]([a-z\d]|[._-](?![._-])))*\.[a-z]{2,}$
```
#### Breakdown of solution

1. ```(?i)```  :- Sets the whole expression to be case-insensitive
2. ```^[a-z\d]```  :- At the start of the string, find a letter (a-z) or number (0-9)
3. ```([a-z\d]|[._-](?![._-]))*```  :- followed by 0 or more characters which can be:
    - a letter (a-z), number (0-9) 
    - OR special character (. or _ or -) as long as it is not followed by another special character. This is achieved using a Negative Lookahead - (?![._-])  
4. ```@```  :- followed by an @
5. ```(\.[a-z\d]([a-z\d]|[._-](?![._-])))*```  :- followed by 0 or unlmited matches of the same pattern described above in point 4., preceded by a "."
6. ```\.``` :- followed by a "."
7. ```[a-z]{2,}$``` :- followed by at least 2 letters, at the end of the string