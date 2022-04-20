# Case Notation
Identify radio network/service (not usually individual stations).

## Description
1. Two characters = ISO 3166-1 two letter country code
1. Two characters = owner type
1. Two characters = service type
1. Two characters = modulation type
1. Unique, sequential case identifier (digits)

A case notation characters might change as details emerge, but the nine digit case identifier will never change.

## Examples
| Scenario                                  | Case Notation |
|-------------------------------------------|---------------|
| NOAA Weather Radio WXL88 near Redding, CA | US GF BS FN   |
| KRDD ATIS (Aviation, City of Redding, CA) | US GL BA AM   |
| KQED FM broadcast station                 | US CC BC FW   |
| Amateur Repeater                          | US PA HR FN   |
| Union Pacific Railroad Dispatch/Train     | US CC LF FN   |
| Unlicensed WiFi                           | US PU WW WF   |

## Country Code (two characters)
Follow [ISO 3166](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)

| Code | Description   |
|------|---------------|
| CA   | Canada        |
| MX   | Mexico        |
| US   | United States |
| UU   | Unknown       |

## Owner Type (two characters)

| Code | Description            |
|------|------------------------|
| CC   | Commercial, Commercial |
| GC   | Government, County     |
| GF   | Government, Federal    |
| GL   | Government, Local      |
| GS   | Government, State      |
| GU   | Government, Unknown    |
| PA   | Private, Amateur       |
| PP   | Private, Pirate        |
| PU   | Private, Unlicensed    |
| UU   | Unknown, Unknown       |

## Service Type (two characters) 

| Code | Description                            |
|------|----------------------------------------|
| AF   | Aviation, Fixed/Mobile                 |
| AN   | Aviation, Navigation Aid               |
| AM   | Aviation, Mobile/Mobile                |
| AU   | Aviation, Unknown                      |
| BA   | Broadcast, Aviation                    |
| BC   | Broadcast, Commercial                  |
| BP   | Broadcast, Paging                      |
| BS   | Broadcast, Safety                      |
| CC   | Cellular, Cellular                     |
| HR   | Amateur Radio, Repeater                |
| LF   | Land, Fixed/Mobile                     |
| MF   | Marine, Fixed/Mobile                   |
| MM   | Microwave, Microwave                   |
| MU   | Microwave, Unknown                     |
| PB   | Personal Communications, Baby Monitors |
| PC   | Personal Communications, CB            |
| PF   | Personal Communications, FRS           |
| PG   | Personal Communications, GMRS          |
| PI   | Personal Communications, Illicit       |
| WW   | Personal Communications, WiFi          |
| RR   | RADAR                                  |

## Modulation Type
| Code | Description                     |
|------|---------------------------------|
| AM   | Amplitude Modulation            |
| FK   | Frequency Shift Keyed TTY       | 
| FN   | Narrowband Frequency Modulation |
| FW   | Wideband Frequency Modulation   |
| MA   | Automatic Morse                 |
| MM   | Manual Morse                    |
| PP   | Pulse                           |
| SL   | Lower Sideband                  |
| SU   | Upper Sideband                  |
| WF   | 802.11 WiFi  
