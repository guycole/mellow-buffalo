# Data Base
SQLite, controlled by Django

## Tables
1. Cases
    1. Case definitions
        | Column     | DataType     | Ndx | Description     |
        |------------|--------------|-----|-----------------|
        | id         | BigAutoField | PK  | Primary key     |
        | country    | CharField(3) |     | Country code    |
        | owner      | CharField(3) |     | Owner type      |
        | service    | CharField(3) |     | Service type    |
        | modulation | CharField(3) |     | Modulation type |

1. CountryCode
    1. Two characters = ISO 3166-1 two letter country code
    1. https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes
        | Column  | DataType      | Ndx | Description  |
        |---------|---------------|-----|--------------|
        | country | CharField(3)  | PK  | Primary key  |
        | name    | CharField(32) |     | Country name |

1. EventLog
    1. Event log
        | Column     | DataType       | Ndx | Description |
        |------------|----------------|-----|-------------|
        | id         | BigAutoField   | PK  | Primary key |
        | time_stamp | DateTimeField  |     | time stamp  |
        | event      | CharField(256) |     | Event text  |

1. ModulationType
    1. Modulation type
        | Column  | DataType      | Ndx | Description  |
        |---------|---------------|-----|--------------|
        | code    | CharField(3)  | PK  | Primary key  |
        | name    | CharField(32) |     | Modulation   |

1. ObsGeoLoc
    1. Observation geographic location
        | Column       | DataType        | Ndx | Description        |
        |--------------|-----------------|-----|--------------------|
        | id           | BigAutoField    | PK  | Primary Key        |
        | host_ts      | BigIntegerField |     | Host Time Stamp    |
        | gps_ts       | BigIntegerField |     | GPS Time Stamp     |
        | altitude     | IntegerField    |     | Altitude * 10      |
        | latitude     | IntegerField    |     | Latitude * 1000    |
        | longitude    | IntegerField    |     | Longitude * 1000   |
        | speed        | IntegerField    |     | Speed * 1000       |
        | track        | IntegerField    |     | Track * 100        |
        | status       | CharField(64)   |     | Fix status         |
        | epx          | IntegerField    |     | EPX * 1000         |
        | epy          | IntegerField    |     | EPY * 1000         |
        | epv          | IntegerField    |     | EPV * 1000         |
        | eps          | IntegerField    |     | EPS * 1000         |
        | epc          | IntegerField    |     | EPC * 1000         |
        | epd          | IntegerField    |     | EPS * 1000         |

1. OwnerType
    1. Network owner
        | Column  | DataType      | Ndx | Description  |
        |---------|---------------|-----|--------------|
        | owner   | CharField(3)  | PK  | Primary key  |
        | name    | CharField(32) |     | Owner type   |

1. ServiceType
    1. Service type
        | Column  | DataType      | Ndx | Description  |
        |---------|---------------|-----|--------------|
        | service | CharField(3)  | PK  | Primary key  |
        | name    | CharField(32) |     | Service type |

1. Tasking
    1. Tasking 
        | Column      | DataType       | Ndx | Description |
        |-------------|----------------|-----|-------------|
        | id          | BigAutoField   | PK  | Primary Key |
        | name        | CharField(32)  |     | Owner type  |
        | description | CharField(256) |     | Event text  |
