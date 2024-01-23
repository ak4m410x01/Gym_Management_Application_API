# Database Tables

##### **Use [dbdiagram](https://dbdiagram.io/d/) to render `models.txt`**

## Accounts

```sql
TABLE accounts {
  id INTEGER [PK, NOT NULL]
  first_name VARCHAR(30) [NOT NULL]
  last_name VARCHAR(30) [NOT NULL]
  gender ENUM('M', 'F') [NOT NULL]
  date_of_birth TIMESTAMP [NOT NULL]
  email EMAIL [UNIQUE, NOT NULL]
  username VARCHAR(100) [UNIQUE, NOT NULL]
  password VARCHAR(100) [NOT NULL]
  country VARCHAR(30) [NULL]
  city VARCHAR(30) [NULL]
  address VARCHAR(50) [NULL]
  image IMAGE [NULL]
  joined_at TIMESTAMP [DEFAULT: `now()`]
  first_login TIMESTAMP [NULL]
  last_login TIMESTAMP [NULL]

  contact_info_id INTEGER [UNIQUE, ref: > contacts_info.id]
}
```

## Admins

```sql
TABLE admins {
  id INTEGER [PK, NOT NULL]
  account_id INTEGER [UNIQUE, ref: > accounts.id]
}
```

## Coaches

```sql
TABLE coaches {
  salary INTEGER [NOT NULL]

  id INTEGER [PK, NOT NULL]
  account_id INTEGER [UNIQUE, ref: > accounts.id]
}
```

## Members

```sql
TABLE members {
  id INTEGER [PK, NOT NULL]
  account_id INTEGER [UNIQUE, ref: > accounts.id]
}
```

## Visitros

```sql
TABLE visitors {
  id INTEGER [PK, NOT NULL]
  account_id INTEGER [UNIQUE, ref: > accounts.id]
}
```

## Contacts Info

```sql
TABLE contacts_info {
  id INTEGER [PK, NOT NULL]
  phone VARCHAR(11) [NULL]
  whatsapp VARCHAR(30) [NULL]
  telegram VARCHAR(30) [NULL]
  facebook VARCHAR(30) [NULL]
  instagram VARCHAR(30) [NULL]
  twitter VARCHAR(30) [NULL]
}
```

---

## Plans

```sql

TABLE plans {
  id INTEGER [PK, NOT NULL]
  title VARCHAR(100) [NOT NULL]
  description VARCHAR(10000) [NULL]
  price INTEGER [NOT NULL]
  created_at TIMESTAMP [DEFAULT: `now()`]
  updated_at TIMESTAMP
}
```

## Subscriptions

```sql

TABLE subscriptions {
  id INTEGER [PK, NOT NULL]
  subscribed_at TIMESTAMP [DEFAULT: `now()`]

  plan_id INTEGER [ref: > plans.id]
  coach_id INTEGER [ref: > coaches.id]
  member_id INTEGER [ref: > members.id]
}

```

## Exercises

```sql

TABLE exercises {
  id INTEGER [PK, NOT NULL]
  title VARCHAR(100) [NOT NULL]
  description VARCHAR(10000)
  done BOOLEAN
  created_at TIMESTAMP [DEFAULT: `now()`]

  coach_id INTEGER [ref: > coaches.id]
  member_id INTEGER [ref: > members.id]
  plan_id INTEGER [ref: > plans.id]
}
```

## Meals

```sql
TABLE meals {
  id INTEGER [PK, NOT NULL]
  title VARCHAR(100) [NOT NULL]
  description VARCHAR(10000) [NULL]
  eat_at TIMESTAMP [NULL]
  done BOOLEAN [NOT NULL]
  created_at TIMESTAMP [DEFAULT: `now()`]

  coach_id INTEGER [ref: > coaches.id]
  member_id INTEGER [ref: > members.id]
  plan_id INTEGER [ref: > plans.id]
}
```

---

## Complaints

```sql

TABLE complaints {
  id INTEGER [PK, NOT NULL]
  title VARCHAR(100) [NOT NULL]
  about VARCHAR(100) [NOT NULL]
  description VARCHAR(10000) [NULL]
  send_to ENUM('admin', 'coach')
  created_at TIMESTAMP [DEFAULT: `now()`]

  member_id INTEGER [ref: > members.id]
}

```

## Vacations

```sql
TABLE vacations {
  id INTEGER [PK, NOT NULL]
  title VARCHAR(100) [NOT NULL]
  description VARCHAR(10000) [NULL]
  reason VARCHAR(10000) [NULL]
  start_at TIMESTAMP [NOT NULL]
  end_at TIMESTAMP [NOT NULL]
  is_accepted BOOLEAN
  created_at TIMESTAMP [DEFAULT: `now()`]

  coach_id INTEGER [ref: > coaches.id]
}

```

---

## Jobs

```sql

TABLE jobs {
  id INTEGER [PK, NOT NULL]
  title VARCHAR(100) [NOT NULL]
  description VARCHAR(10000) [NULL]
  requirements VARCHAR(10000) [NULL]
  details VARCHAR(10000) [NULL]
  skills VARCHAR(10000) [NULL]
  available BOOLEAN [NOT NULL]
  created_at TIMESTAMP [DEFAULT: `now()`]
}

```

## Job applicants

```sql
TABLE job_applicants {
  status ENUM('refused', 'accepted')
  created_at TIMESTAMP [DEFAULT: `now()`]

  job_id INTEGER [PK, ref: > jobs.id]
  applicant INTEGER [PK, ref: > accounts.id]
}
```

---

## Contact Us

```sql
TABLE contact_us {
  id INTEGER [PK, NOT NULL]
  country VARCHAR(30) [NULL]
  city VARCHAR(30) [NULL]
  address VARCHAR(50) [NULL]
  email EMAIL [NULL]
  phone VARCHAR(11) [NULL]
  whatsapp VARCHAR(30) [NULL]
  telegram VARCHAR(30) [NULL]
  facebook VARCHAR(30) [NULL]
  instagram VARCHAR(30) [NULL]
  twitter VARCHAR(30) [NULL]
}

```

## About us

```sql

TABLE about_us {
  id INTEGER [PK, NOT NULL]
  the_face_of_your_business VARCHAR(20000) [NULL]
  who_are_serve VARCHAR(20000) [NULL]
  our_mission VARCHAR(20000) [NULL]
  our_goals VARCHAR(20000) [NULL]
}

```
