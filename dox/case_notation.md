# Case Notation
Identify radio network/service (not usually individual stations).

## Description
1. Two characters = ISO 3166-1 two letter country code
1. Two characters = owner type
1. Two characters = service type
1. Two characters = modulation type
1. One character = network type
1. Nine digits = unique, sequential case identifier

A case notation characters might change as details emerge, but the nine digit case identifier will never change.

## Examples
| Scenario | Case Notation |
| NOAA Weather Radio WXL88 near Redding, CA | USAXXFNX000000001 |
| KRDD ATIS (Aviation)                      | USAXXAMX000000001 |
| KQED FM broadcast station                 | USAXXFWX000000001 |
| Amateur Repeater                          | USAXXFN0000000001 |
| Union Pacific Railroad                    | USAXXFN0000000001 |
| Unlicensed WiFi                           | USAXXWF0000000001 |
Radar
Microwave
Family Radio

## Country Code (two characters)
Follow [ISO 3166](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)

| Code | Description |
|------|-------------|
| UU   | Unknown     |

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
| AB   | Aviation, Broadcast                    |
| AF   | Aviation, Fixed/Mobile                 |
| AN   | Aviation, Navigation Aid               |
| AM   | Aviation, Mobile/Mobile                |
| AU   | Aviation, Unknown                      |
| BB   | Broadcast, Broadcast                   |
| BP   | Broadcast, Paging                      |
| CC   | Cellular, Cellular                     |
| LF   | Land, Fixed/Mobile                     |
| MF   | Marine, Fixed/Mobile                   |
| MM   | Microwave, Microwave                   |
| MU   | Microwave, Unknown                     |
| PB   | Personal Communications, Baby Monitors |
| PC   | Personal Communications, CB            |
| PF   | Personal Communications, FRS           |
| PG   | Personal Communications, GMRS          |
| PI   | Personal Communications, Illicit       |

## Modulation Type
| Code | Description                     |
|------|---------------------------------|
| AM   | Amplitude Modulation            |
| FK   | Frequency Shift Keyed TTY       | 
| FN   | Narrowband Frequency Modulation |
| FW   | Wideband Frequency Modulation   |
| MA   | Automatic Morse                 |
| MM   | Manual Morse                    |
| SL   | Lower Sideband                  |
| SU   | Upper Sideband                  |
| WF   | 802.11 WiFi  

## Service Code [see also](https://www.fcc.gov/radio-services)
| Service Code | Group                         | Description                                                                   |
|--------------|-------------------------------|-------------------------------------------------------------------------------|
| AA           | Coast and Ground              | Aviation Auxiliary Group                                                      |
| AB           | XX                            | Aural Microwave Booster                                                       |
| AC           | Aircraft/AV                   | Aircraft                                                                      |
| AF           | Coast and Ground              | Aeronautial and Fixed                                                         |
| AI           | XX                            | Aural Intercity Relay                                                         |
| AR           | Coast and Ground              | Aviation Radionavigation                                                      |
| AS           | XX                            | Aural Studio Transmitter Link                                                 |
| AW           | XX                            | AWS 1710-1755 MHz/2110-2155 MHz                                               |
| BA           | XX                            | 1390-1392 MHz, Market Area                                                    |
| BB           | XX                            | 1392-1395 MHz/1432-1435 MHz, Market Area                                      |
| BC           | Land Mobile Private           | 1670-1675 MHz, Market Area                                                    |
| BR           | Broadband Radio Service       | Broadband Radio Service                                                       |
| CA           | Paging                        | Commerical Air-Ground Radiotelephone                                          |
| CB           | Paging                        | BETRS                                                                         |
| CD           | Paging                        | Paging and Radiotelephone                                                     |
| CE           | XX                            | Digital Electronic Message Service (Common Carrier)                           |
| CF           | XX                            | Common Carrier Fixed Point to Point Microwave                                 |
| CG           | Paging                        | General Aviation Air-Ground Radiotelephone                                    |
| CJ           | Paging                        | Commercial Aviation Air-Ground Radiotelephone                                 |
| CL           | Cellular                      | Cellular                                                                      |
| CM           | Commercial and Restricted     | Commercial Operator                                                           |
| CN           | XX                            | PCS Narrowband                                                                |
| CO           | Paging                        | Offshore Radiotelephone                                                       |
| CP           | Paging                        | Part 22 VHF/UHF Paging (exclude 931 MHz)                                      |
| CR           | Paging                        | Rural Radiotelephone                                                          |
| CT           | XX                            | Local Television Transmission                                                 |
| CW           | XX                            | PCS Broadband                                                                 |
| CY           | XX                            | 1910-1915 MHz/1990-1995 MHz, Market Area                                      |
| CZ           | Paging                        | Paging and Radiotelephone, Auctioned                                          |
| DV           | XX                            | Multichannel Video Distribution and Data Service                              |
| ED           | Educational Broadband Service | Educational Broadband Service                                                 |
| GB           | XX                            | Business 806-821 MHz | 851-866 MHz Conventional                               |
| GC           | Paging                        | 921-931 MHz, Auctioned                                                        |
| GI           | XX                            | Other Industrial/Land Transportation 896-901 MHz/935-940 MHz, Conventional    |
| GJ           | XX                            | Business/Industrial/Land Transportation 809-824 MHz/854-869 MHz, Conventional |
| GL           | Land Mobile Commercial        | 900 MHz Conventional SMR                                                      |
| GM           | Land Mobile Commercial        | 800 MHz Conventional SMR                                                      |
| GO           | XX                            | Other Industrial/Land Transportation 806-821 MHz/851-866 MHz, Conventional    |
| GR           | Land Mobile Commercial        | 896-901 MHz/935-940 MHz Conventional SMR                                      |
| GS           | Land Mobile Commercial        | Private Carrier Paging 929-930 MHz                                            | 
| GU           | XX                            | Business 896-901 MHz, Conventional                                            |
| GX           | Land Mobile Commerical        | 806-821 MHz/851-866 MHz Conventional SMR                                      |
| HA           | Amateur                       | Amateur (Ham Radio)                                                           |
| IG           | XX                            | Industrial/Business Pool, Conventional                                        |
| IK           | Land Mobile Commercial        | Industrial/Business Pool, Commercial, Conventional                            |
| LD           | XX                            | Local Multipoint Distribution Service                                         |
| LP           | XX                            | Broadcast Auxiliary Low Power                                                 |
| LN           | Land Mobile Commercial        | 902-928 MHz Location Narrowband (non-multilateration)                         |
| LS           | Land Mobile Commercial        | Location and Monitoring Service, Multilateration (LMS)                        |
| LV           | XX                            | Low Power Wireless Assist Video Devices                                       |
| LW           | Land Mobile Commercial        | 902-928 MHz Location Wideband (Grandfathered AVM)                             |
| MA           | Coast and Ground              | Marine Auxiliary Group                                                        |
| MC           | Coast and Ground              | Coastal Group                                                                 |
| MG           | XX                            | Microwave Industrial/Business Pool                                            |
| MK           | Coast and Ground              | Alaska Group                                                                  |
| MM           | XX                            | Millimeter Wave 70-80-90 GHz                                                  |
| MR           | Coast and Ground              | Marine Radiolocation Land                                                     |
| MS           | XX                            | Multiple Address Service, Auctioned                                           |
| NC           | Land Mobile Commercial        | Nationwide commercial 5 Channel, 220 MHz                                      |
| NN           | XX                            | 3650-3700 MHz                                                                 |
| PC           | Coast and Ground              | Public Coast Stations, Auctioned                                              |
| PE           | XX                            | Digital Electronic Message Service (Private Operational Fixed)                |
| QA           | Land Mobile Commercial        | 220-222 MHz Band, Auctioned                                                   |
| QD           | Land Mobile Commercial        | Non-Nationwide Data, 220 MHz                                                  |
| QO           | Land Mobile Commercial        | Non-Nationwide Other, 220 MHz                                                 |
| QQ           | XX                            | Intelligent Transportation Service (Non-Public Safety)                        |
| QT           | Land Mobile Commercial        | Non-Nationwide 5 Channel Trunked, 220 MHz                                     |
| RP           | XX                            | Broadcast Auxiliary Remote Pickup                                             |
| RR           | Commercial and Restricted     | Restricted Operator                                                           |
| RS           | XX                            | Land Mobile Radiolocation                                                     |
| SA           | Ship                          | Ship Recreational or Voluntarily Equipped                                     |
| SB           | Ship                          | Ship compulsory Equipped                                                      |
| SE           | Ship                          | Ship Exemption                                                                |
| TB           | XX                            | TV Microwave Booster                                                          |
| TI           | XX                            | TV Intercity Relay                                                            |
| TN           | XX                            | 39 GHz Auctioned                                                              |
| TP           | XX                            | TV Pickup                                                                     |
| TS           | XX                            | TV Studio Transmitter Link                                                    |
| TT           | XX                            | TV Translator Relay                                                           |
| TZ           | XX                            | 24 GHz Service                                                                |
| UU           | XX                            | Upper Microwave Flexible Use Service UMFUS                                    |
| WA           | XX                            | Microwave Aviation                                                            |
| WM           | XX                            | Microwave Marine                                                              |
| WR           | XX                            | Microwave Radiolocation                                                       |
| WP           | XX                            | 700 MHz Upper Band                                                            |
| WS           | XX                            | Wireless Communications Service                                               |
| WU           | XX                            | 700 MHz Upper Band                                                            |
| WX           | XX                            | 700 MHz Guard Band                                                            |
| WY           | XX                            | 700 MHz Lower Band                                                            |
| WZ           | XX                            | 700 MHz Lower Band                                                            |
| YB           | XX                            | Business 806-821 MHz/851-866 MHz Trunked                                      |
| YC           | Land Mobile Commercial        | SMR 806-821 MHz/851-866 MHz, Auctioned                                        |
| YD           | Land Mobile Commercial        | SMR 896-901 MHz/935-940 MHz, Auctioned                                        |
| YG           | XX                            | Industrial/Business Pool, Trunked                                             |
| YH           | Land Mobile Commercial        | SMR 806-821 MHz/851-866 MHz, Auctioned                                        |
| YI           | xX                            | Other Industrial/Land Transportation 806-821 MHz/935-940 MHz, Trunked         |
| YJ           | XX                            | Business/Industrial/Land Transportation 809-821 MHz/854-869 MHz, Trunked      |
| YK           | Land Mobile Commercial        | Industrial/Business Pool - Commercial, Trunked                                |
| YM           | Land Mobile Commercial        | 800 MHz Trunked SMR (SMR, Site Specific)                                      |
| YO           | XX                            | Other Industrial/Land Transportation 806-821 MHz/851-866 MHz, Trunked         |
| YS           | Land Mobile Commercial        | SMR, 896-901 MHz/935-940 MHz, Trunked                                         |
| YU           | XX                            | Busines 896-901 MHz/935-940 MHz, Trunked                                      |
| YX           | Land Mobile Commercial        | SMR, 806-821 MHz/851-866 MHz, Trunked                                         |
| ZA           | GMRS                          | General Mobile Radio Services GMRS                                            |
| ZV           | XX                            | Formerly IVDS now 218-219 MHz                                                 |


 

 

Third Letter = Service

A = Amateur
C = Commercial
G = Government
S = Merchant Shipping
U = Unlicensed

Fourth Letter = Link type
A = Morse
B
C
D
E
N = Narrowband FM

