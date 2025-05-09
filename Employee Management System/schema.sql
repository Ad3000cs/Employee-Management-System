-- PRAGMA table_info(details);
-- DROP TABLE IF EXISTS details;
-- DROP TABLE IF EXISTS Bank_details;
-- DROP TABLE IF EXISTS Salary;

-- CREATE TABLE details(
-- ID TEXT(5) PRIMARY KEY,
-- First_name TEXT (30),
-- Last_name TEXT (30),
-- E_mail TEXT(100),
-- Phone_Number TEXT (14),
-- Address TEXT,
-- County TEXT,
-- Join_date DATE,
-- Department TEXT (30),
-- Role TEXT (30),
-- Type TEXT(20),
-- Salary_CTC DECIMAL,
-- level TEXT,
-- Total_leaves INT (20),
-- Taken_leaves INT(20),
-- Left_leaves INT(20),
-- Termination_date DATE );

-- CREATE TABLE Bank_details(
-- ID TEXT(5) PRIMARY KEY,
-- First_name TEXT (30),
-- Last_name TEXT (30),
-- Bank TEXT(30),
-- Branch TEXT(30),
-- IBAN TEXT(20),
-- Account_Number TEXT,
-- PSC TEXT );

-- CREATE TABLE Salary(
-- ID TEXT(5) PRIMARY KEY,
-- CTC DECIMAL (40),
-- House_rent_allowance DECIMAL (40),
-- Travel_allowance DECIMAL (40),
-- Taxable_income DECIMAL (40),
-- Tax_rate DECIMAL (40),
-- In_hand DECIMAL (40));

-- NOTE - IF REQUIRED THE FOLLOWING 2 QUERIES ARE TO BE RUN SIMULTANEOUSLY


-- INSERT INTO details (ID, First_name, Last_name, E_mail, Phone_Number, Address, County, Join_date, Department, Role, Type, level, Total_leaves, Taken_leaves, Left_leaves)
-- VALUES 
-- ('E02', 'Nathon', 'Starc', 'nstarc@gmail.com', '+353 854363432', 'House 14, Washington Road', 'Cork', '2021-05-01', 'Software Development', 'AI Engineer', 'Permanent', 92000.00, 'Mid level', 30, 7, 23),
-- ('E03', 'Cameron', 'Green', 'Camgreen@gmail.com', '+353 874059438', 'House 98, College Road', 'Cork', '2023-01-03', 'Hardware Intigration', 'Engineer', 'Permanent', 40000.00, 'Junior', 30, 20, 10),
-- ('E04', 'Pat', 'Lyon', 'patlyon@gmail.com', '+353 884351032', 'House 9, Currahen Road', 'Dublin', '2019-05-15', 'Software Development', 'Developer', 'Permanent', 172000.00, 'Senior', 30, 2, 28),
-- ('E05', 'Jason', 'Roy', 'jasonroy@gmail.com', '+353 870350432', 'House 93, City Centre', 'Dublin', '2020-07-01', 'Hardware Integration', 'Tester', 'Permanent', 50000.00, 'Mid level', 30, 1, 29),
-- ('E06', 'Chris', 'Martin', 'chrismartin@gmail.com', '+353 87435000', 'House 1, City Centre', 'Dublin', '2022-06-20', 'Software Development', 'Developer', 'Permanent', 90000.00, 'Mid Level', 30, 9, 21),
-- ('E07', 'Jos', 'Butler', 'jbutler@gmail.com', '+353 805357432', 'House 12, City Centre', 'Tralee', '2023-04-03', 'Business Management', 'Accountant', 'Permanent', 75000.00, 'Mid level', 30, 14, 16),
-- ('E08', 'Eoin', 'Jordan', 'eoinjordan@gmail.com', '+353 808907432', 'House 114, City Centre', 'Tralee', '2022-02-03', 'Business Management', 'Analyst', 'Permanent', 85000.00, 'Mid level', 30, 11, 19),
-- ('E09', 'Jhonny', 'Latin', 'jonnylatin@gmail.com', '+353 805321322', 'House 19, Mardyke Road', 'Kinsley', '2018-09-05', 'Software Development', 'Developer', 'Permanent', 180000.00, 'Senior', 30, 1, 29),
-- ('E10', 'Jhon', 'Leach', 'jhonleach@gmail.com', '+353 805377322', 'House 21, Tree Road', 'Dublin', '2018-09-05', 'Sales and Marketing', 'Sales and Marketing Manager', 'Permanent', 110000.00, 'Senior', 30, 12, 18);

-- INSERT INTO details (ID, First_name, Last_name, E_mail, Phone_Number, Address, County, Join_date, Department, Role, Type, level, Total_leaves, Taken_leaves, Left_leaves, Termination_date)
-- VALUES
-- ('E11', 'Trent', 'Guptill', 'trentguptill@gmail.com', '+353 835344488', 'House 12, Tailor Road', 'Tralee', '2024-01-03', 'Sales and Marketing', 'Sales Associate', 'Freelance', 'Mid level', 20, 2, 18, '2026-01-03'),
-- ('E12', 'Tim', 'Southee', 'southeetim@gmail.com', '+353 835399988', 'House 19, Tailor Road', 'Kinsley', '2024-02-05', 'Sales and Marketing', 'Digital Marketer', 'Freelance', 'Mid level', 20, 3, 17, '2026-02-05'),
-- ('E13', 'Tom', 'Boult', 'boulttom@gmail.com', '+353 835559988', 'House 31, Carter Road', 'Dublin', '2023-02-05', 'Sales and Marketing', 'Sales Associate', 'Freelance', 'Mid level', 20, 3, 17, '2025-02-05'),
-- ('E14', 'Kim', 'Bradman', 'k.bradman@gmail.com', '+353 805377559', 'House 121, Flower Road', 'Kinsley', '2023-09-05', 'Business Management', 'Auditor', 'Freelance', 'Senior', 30, 10, 20, '2025-09-05');







-- INSERT INTO Bank_details (ID, First_name, Last_name, Bank, Branch, IBAN, Account_Number, PSC) 
-- VALUES
-- ('E02', 'Nathon', 'Starc', 'BOI', 'UCC Quad', 'IE96BOI989902279802', '1129805467', 'IE2793567E'),
-- ('E03', 'Cameron', 'Green', 'AIB', 'St Patricks Street', 'IE97AIB999582815575', '1129809879', 'IE2423798E'),
-- ('E04', 'Pat', 'Lyon', 'BOI', 'TCD Campus', 'IE95BOI999809864181', '1129800073', 'IE2423007E'),
-- ('E05', 'Jason', 'Roy', 'AIB', 'City Centre', 'IE95AIB995855864181', '1124539873', 'IE2422297E'),
-- ('E06', 'Chris', 'Martin', 'BOI', 'City Centre', 'IE95BOI997829864181', '1165809873', 'IE1953567E'),
-- ('E07', 'Jos', 'Butler', 'AIB', 'Quad Road', 'IE95AIB995823334181', '1122109873', 'IE2013567E'),
-- ('E08', 'Eoin', 'Jordan', 'BOI', 'City Centre', 'IE95BOI995829777181', '6569809873', 'IE2425567E'),
-- ('E09', 'Jhonny', 'Latin', 'AIB', 'Mardyke Road', 'IE95AIB885829864181', '1129989873', 'IE2427767E'),
-- ('E10', 'Jhon', 'Leach', 'AIB', 'Tree Road', 'IE95AIB995829756481', '1123132873', 'IE2423317E'),
-- ('E11', 'Trent', 'Guptill', 'AIB', 'Tailer Road', 'IE95AIB995829879881', '1129809993', 'IE2423007E'),
-- ('E12', 'Tim', 'Southee', 'BOI', 'Tailor Road', 'IE95BOI995829864271', '1177709873', 'IE2420007E'),
-- ('E13', 'Tom', 'Boult', 'BOI', 'Carter Road', 'IE95BOI995000864181', '1129009873', 'IE0423567E'),
-- ('E14', 'Kim', 'Bradman', 'AIB', 'Flower Road', 'IE95AIB990029864181', '1123009873', 'IE2100567E');

-- INSERT INTO Salary(ID, CTC, House_rent_allowance, Travel_allowance, Taxable_income, Tax_rate, In_hand)
-- VALUES
-- ('E02', 92000.00, 12000.00, 5000.00, 75000.00, 30.00, 52500.00),
-- ('E03', 40000.00, 8000.00, 3000.00, 29000.00, 40.00, 17400.00),
-- ('E04', 172000.00, 15000.00, 7000.00, 150000.00, 20.00, 120000.00),
-- ('E05', 50000.00, 10000.00, 6000.00, 36000.00, 30.00, 25200.00),
-- ('E06', 90000.00, 11000.00, 5000.00, 74000.00, 30.00, 51800.00),
-- ('E07', 75000.00, 11000.00, 4000.00, 60000.00, 30.00, 42000.00),
-- ('E08', 85000.00, 12000.00, 4000.00, 69000.00, 30.00, 48300.00),
-- ('E09', 180000.00, 16000.00, 8000.00, 156000.00, 20.00, 124800.00),
-- ('E10', 110000.00, 11000.00, 6000.00, 93000.00, 20.00, 74400.00),
-- ('E11', 65000.00, 8000.00, 7000.00, 50000.00, 30.00, 35000.00),
-- ('E12', 60000.00, 8000.00, 5000.00, 47000.00, 30.00, 32900.00),
-- ('E13', 60000.00, 8000.00, 5000.00, 47000.00, 30.00, 32900.00),
-- ('E14', 91000.00, 11000.00, 9000.00, 71000.00, 20.00, 56800.00);



-- DROP TABLE IF EXISTS emplogininfo;

-- CREATE TABLE emplogininfo(
-- empID TEXT PRIMARY KEY,
-- loginID TEXT,
-- Password TEXT);

-- INSERT INTO emplogininfo(empID, loginID, Password)
-- VALUES
-- ('E02', 'Nathon', 'EMSE02'),
-- ('E03', 'Cameron', 'EMSE03'),
-- ('E04', 'Pat', 'EMSE04'),
-- ('E05', 'Jason', 'EMSE05'),
-- ('E06', 'Chris', 'EMSE06'),
-- ('E07', 'Jos', 'EMSE07'),
-- ('E08', 'Eoin', 'EMSE08'),
-- ('E09', 'Jhonny', 'EMSE09'),
-- ('E10', 'Jhon', 'EMSE10'),
-- ('E11', 'Trent', 'EMSE11'),
-- ('E12', 'Tim', 'EMSE12'),
-- ('E13', 'Tom', 'EMSE13'),
-- ('E14', 'Kim', 'EMSE14');

-- DROP TABLE IF EXISTS Admin;

-- CREATE TABLE Admin(
-- ID TEXT PRIMARY KEY,
-- Password TEXT);

-- INSERT INTO Admin(ID, Password) VALUES ('am03', 'am201');

-- SELECT * FROM emplogininfo;