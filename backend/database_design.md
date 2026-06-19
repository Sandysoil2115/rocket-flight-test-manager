## User Table

| Column | Type | Key |
|---------|----|----|
| Id | Integer | primary key |
| name | String | - |
| Username| String | - |
| Email | String | Unique |
| Password | String (hashed)| - |
| Created_At | Time | - |

## Flight_test
| Column | Type | Key |
|--------|-----|----|
| Id | Integer | Primary key |
| Name | String | - |
| Date | Date | - |
| Weight (g) | Float | - |
| Launch Angle | Float | - |
| Max Alt (m) | Float | - |
| Max Vel (m/s) | Float | - |
| Lauch acceleration (m/s2) | Float | - |
| Thrust (N) | Float | - |
| Status | String | - |
| Reasons | String | - |
| Owner_id | Integer | Foreign key -> Users.id |
| Created_At | Time | - |

## Media
| Column | Type | Key |
|--------|-----|----|
| Id | Integer | Primary key |
| Name | String | - |
| Type | String | - |
| File_Path | String | - |
| flight_test | Integer | Foreign key -> Flight_tests.id |
| Uploaded_At | Time | - |