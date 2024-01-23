-- Active: 1703942992435@@127.0.0.1@5432@gym@public
-- -------------------------- --
-- =======> Accounts <======= --
-- -------------------------- --
-- Contacts
DROP Table IF EXISTS contacts;

CREATE Table contacts (
    id SERIAL NOT NULL,
    phone VARCHAR(11) NULL,
    whatsapp VARCHAR(30) NULL,
    telegram VARCHAR(30) NULL,
    facebook VARCHAR(30) NULL,
    instagram VARCHAR(30) NULL,
    twitter VARCHAR(30) NULL,
    -- Keys
    PRIMARY KEY(id)
);

-- Accounts
DROP TABLE IF EXISTS accounts;

CREATE Table accounts (
    id SERIAL NOT NULL,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    gender CHAR(1) CHECK(gender IN('M', 'F')),
    date_of_birth DATE,
    email VARCHAR(100) UNIQUE NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    country VARCHAR(30) NULL,
    city VARCHAR(30) NULL,
    address VARCHAR(50) NULL,
    image VARCHAR(1000) NULL,
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    first_login TIMESTAMP NULL,
    last_login TIMESTAMP NULL,
    contact_id INTEGER NOT NULL UNIQUE,
    -- Keys
    PRIMARY KEY(id),
    Foreign Key (contact_id) REFERENCES contacts(id)
);

-- Admins
DROP TABLE IF EXISTS admins;

CREATE Table admins (
    id SERIAL NOT NULL,
    account_id INTEGER NOT NULL UNIQUE,
    -- Keys
    PRIMARY KEY(id),
    Foreign Key (account_id) REFERENCES accounts(id)
);

-- Coaches
DROP TABLE IF EXISTS coaches;

CREATE Table coaches (
    id SERIAL NOT NULL,
    salary INTEGER NOT NULL,
    account_id INTEGER NOT NULL UNIQUE,
    -- Keys
    PRIMARY KEY(id),
    Foreign Key (account_id) REFERENCES accounts(id)
);

-- Members
DROP TABLE IF EXISTS members;

CREATE Table members (
    id SERIAL NOT NULL,
    account_id INTEGER NOT NULL UNIQUE,
    -- Keys
    PRIMARY KEY(id),
    Foreign Key (account_id) REFERENCES accounts(id)
);

-- Visitors
DROP TABLE IF EXISTS visitors;

CREATE Table visitors (
    id SERIAL NOT NULL,
    account_id INTEGER NOT NULL UNIQUE,
    -- Keys
    PRIMARY KEY(id),
    Foreign Key (account_id) REFERENCES accounts(id)
);

-- Salaries
DROP TABLE IF EXISTS coaches_salaries;

CREATE TABLE coaches_salaries (
    id SERIAL NOT NULL,
    salary INTEGER NOT NULL,
    coach_id INTEGER NOT NULL UNIQUE,
    -- Keys
    PRIMARY KEY(id),
    Foreign Key (coach_id) REFERENCES coaches(id)
);

-- =================================================================
-- -------------------------- --
-- =======> Plans <======= --
-- -------------------------- --
-- Plans
DROP TABLE IF EXISTS plans;

CREATE TABLE plans(
    id SERIAL NOT NULL,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(10000) NOT NULL,
    price INTEGER DEFAULT 0,
    classes INTEGER DEFAULT 0,
    max_days INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP,
    -- Keys
    PRIMARY KEY(id)
);

-- Subscriptions
DROP TABLE IF EXISTS subscriptions;

CREATE TABLE subscriptions(
    id SERIAL NOT NULL,
    subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_finished BOOLEAN DEFAULT False,
    plan_id INTEGER NOT NULL,
    coach_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    -- Keys
    PRIMARY KEY(id),
    Foreign Key (plan_id) REFERENCES plans(id),
    Foreign Key (coach_id) REFERENCES coaches(id),
    Foreign Key (member_id) REFERENCES members(id)
);

-- Exercises
DROP TABLE IF EXISTS exercises;

CREATE TABLE exercises(
    id SERIAL NOT NULL,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(10000) NOT NULL,
    eat_at TIMESTAMP NULL,
    done BOOLEAN DEFAULT False,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    plan_id INTEGER NOT NULL,
    coach_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    -- Keys
    PRIMARY KEY(id),
    Foreign Key (plan_id) REFERENCES plans(id),
    Foreign Key (coach_id) REFERENCES coaches(id),
    Foreign Key (member_id) REFERENCES members(id)
);

-- Meals
DROP TABLE IF EXISTS meals;

CREATE TABLE meals(
    id SERIAL NOT NULL,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(10000) NOT NULL,
    eat_at TIMESTAMP NULL,
    done BOOLEAN DEFAULT False,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    plan_id INTEGER NOT NULL,
    coach_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    -- Keys
    PRIMARY KEY(id),
    Foreign Key (plan_id) REFERENCES plans(id),
    Foreign Key (coach_id) REFERENCES coaches(id),
    Foreign Key (member_id) REFERENCES members(id)
);

-- =================================================================
-- -------------------------- --
-- =======> Support <======= --
-- -------------------------- --
-- Complaints
DROP TABLE IF EXISTS complaints;

CREATE TABLE complaints(
    id SERIAL NOT NULL,
    title VARCHAR(100) NOT NULL,
    about VARCHAR(100) NOT NULL,
    description VARCHAR(10000) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    member_id INTEGER NOT NULL,
    -- 1: Not Seen
    -- 2: Seen
    status INTEGER CHECK(status in(1, 2)) DEFAULT 1,
    -- Keys
    PRIMARY KEY(id),
    Foreign Key (member_id) REFERENCES members(id)
);

-- Vacations
DROP TABLE IF EXISTS vacations;

CREATE TABLE vacations(
    id SERIAL NOT NULL,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(10000) NULL,
    reason VARCHAR(10000) NULL,
    start_at TIMESTAMP NOT NULL,
    end_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    coach_id INTEGER NOT NULL,
    -- 1: Not Seen
    -- 2: Seen
    -- 3: Refused
    -- 4: Accepted
    status INTEGER CHECK(status in(1, 2, 3, 4)) DEFAULT 1,
    -- Keys
    PRIMARY KEY(id),
    Foreign Key (coach_id) REFERENCES coaches(id)
);

-- =================================================================
-- -------------------------- --
-- =======> Jobs <======= --
-- -------------------------- --
-- Jobs
DROP Table IF EXISTS jobs;

CREATE TABLE jobs (
    id SERIAL NOT NULL,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(10000) NULL,
    requirements VARCHAR(10000) NULL,
    details VARCHAR(10000) NULL,
    skills VARCHAR(10000) NULL,
    is_available BOOLEAN DEFAULT True,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    -- Keys
    PRIMARY KEY(id)
);

-- Jobs Applicants
DROP TABLE IF EXISTS job_applicants;

CREATE TABLE job_applicants (
    job_id INTEGER NOT NULL,
    applicant INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    -- 1: Not Seen
    -- 2: Seen
    -- 3: Refused
    -- 4: Accepted
    status INTEGER CHECK(status in(1, 2, 3, 4)) DEFAULT 1,
    PRIMARY KEY(job_id, applicant),
    Foreign Key (job_id) REFERENCES jobs(id),
    Foreign Key (applicant) REFERENCES accounts(id)
);

-- =================================================================
-- -------------------------- --
-- =======> Settings <======= --
-- -------------------------- --
-- Contact us
DROP Table IF EXISTS contact_us;

CREATE TABLE contact_us(
    id SERIAL NOT NULL,
    country VARCHAR(30) NULL,
    city VARCHAR(30) NULL,
    address VARCHAR(50) NULL,
    email VARCHAR(50) NULL,
    phone VARCHAR(11) NULL,
    whatsapp VARCHAR(30) NULL,
    telegram VARCHAR(30) NULL,
    facebook VARCHAR(30) NULL,
    instagram VARCHAR(30) NULL,
    twitter VARCHAR(30) NULL,
    -- Keys
    PRIMARY KEY(id)
);

-- About us
DROP Table IF EXISTS about_us;

CREATE TABLE about_us(
    id SERIAL NOT NULL,
    the_face_of_your_business VARCHAR(20000) NULL,
    who_are_serve VARCHAR(20000) NULL,
    our_mission VARCHAR(20000) NULL,
    our_goals VARCHAR(20000) NULL,
    -- Keys
    PRIMARY KEY(id)
);