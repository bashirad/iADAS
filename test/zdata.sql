drop table rainlogger;
drop table levelogger;
drop table notification;

create table notification (
    employeeID INT NOT NULL AUTO_INCREMENT,
    firstName LONGTEXT NOT NULL,
    lastName LONGTEXT NOT NULL,
    email LONGTEXT NOT NULL,
    phoneNum LONGTEXT NOT NULL,
    PRIMARY KEY (employeeID)
);

create table rainlogger(
    id int AUTO_INCREMENT,
    dateTime datetime not null,
    rainFallInMilliMeters float not null,
    primary key(id)
);

create table levelogger(
    id int AUTO_INCREMENT,
    dateTime datetime not null,
    levelInMeters float not null,
    primary key(id)
);

INSERT INTO rainlogger(datetime, rainFallInMilliMeters)
VALUES 
('2020-01-01 06:00:00', 6),
('2021-02-02 06:00:00', 6),
('2021-04-03 07:00:00', 10),
('2022-06-04 08:00:00', 12),
('2022-07-05 09:00:00', 17),
('2022-08-06 06:00:00', 12),
                            ('2022-09-01 06:00:00', 6),
                            ('2022-09-02 06:00:00', 6),
                            ('2022-09-03 07:00:00', 10),
                            ('2022-09-04 08:00:00', 12),
                            ('2022-09-05 09:00:00', 17),
                            ('2022-09-06 06:00:00', 12),
                            ('2022-09-07 06:00:00', 6),
                            ('2022-09-08 06:00:00', 6),
                            ('2022-09-09 07:00:00', 10),
                            ('2022-09-10 08:00:00', 12),
                            ('2022-09-11 09:00:00', 17),
                            ('2022-09-12 06:00:00', 12),
                            ('2022-09-13 08:00:00', 13),
                            ('2022-09-14 07:00:00', 9),
                            ('2022-09-15 08:00:00', 11),
                            ('2022-09-16 09:00:00', 17),
                            ('2022-09-17 06:00:00', 6),
                            ('2022-09-18 06:00:00', 6),
                            ('2022-09-19 07:00:00', 10),
                            ('2022-09-20 08:00:00', 12),
                            ('2022-09-21 09:00:00', 17),
                            ('2022-09-22 06:00:00', 12),
                            ('2022-09-23 06:00:00', 6),
                            ('2022-09-24 06:00:00', 6),
                            ('2022-09-25 07:00:00', 10),
                            ('2022-09-26 08:00:00', 12),
                            ('2022-09-27 09:00:00', 17),
                            ('2022-09-28 06:00:00', 12),
                            ('2022-09-29 08:00:00', 13),
                            ('2022-09-30 07:00:00', 9),
                            ('2022-10-01 08:00:00', 11),
                                                        ('2022-10-02 09:00:00', 17),
                                                        ('2022-10-02 08:00:00', 11),
                                                        ('2022-10-03 09:00:00', 17),
                                                        ('2022-10-04 08:00:00', 11),
                                                        ('2022-10-05 09:00:00', 17),
                                                        ('2022-10-06 08:00:00', 11),
                                                        ('2022-10-07 09:00:00', 17),
                                                        ('2022-10-08 08:00:00', 11),
                                                        ('2022-10-09 09:00:00', 17),
                                                        ('2022-10-10 08:00:00', 11),
                                                        ('2022-10-11 09:00:00', 17),
                                                        ('2022-10-12 08:00:00', 11),
                                                        ('2022-10-13 09:00:00', 17),
                                                        ('2022-10-14 08:00:00', 11),
                                                        ('2022-10-15 09:00:00', 17),
                                                        ('2022-10-16 08:00:00', 11),
                                                        ('2022-10-17 09:00:00', 17),
                                                        ('2022-10-18 08:00:00', 11),
                                                        ('2022-10-19 09:00:00', 17),
                                                        ('2022-10-20 08:00:00', 11),
                                                        ('2022-10-21 06:00:00', 12),
                                                                                       ('2022-11-01 08:00:00', 11),
                                                                                       ('2022-11-02 09:00:00', 17),
                                                                                       ('2022-11-02 08:00:00', 11),
                                                                                       ('2022-11-03 09:00:00', 17),
                                                                                       ('2022-11-04 08:00:00', 11),
                                                                                       ('2022-11-05 09:00:00', 17),
                                                                                       ('2022-11-06 08:00:00', 11),
                                                                                       ('2022-11-07 09:00:00', 17),
                                                                                       ('2022-11-08 08:00:00', 11),
                                                                                       ('2022-11-09 09:00:00', 17),
                                                                                       ('2022-11-10 08:00:00', 11),
                                                                                       ('2022-11-11 09:00:00', 17),
                                                                                       ('2022-11-12 08:00:00', 11),
                                                                                       ('2022-11-13 09:00:00', 17),
                                                                                       ('2022-11-14 08:00:00', 11),
                                                                                       ('2022-11-15 09:00:00', 17),
                                                                                       ('2022-11-16 08:00:00', 11),
                                                                                       ('2022-11-17 09:00:00', 17),
                                                                                       ('2022-11-18 08:00:00', 11),
                                                                                       ('2022-11-19 09:00:00', 17),
                                                                                       ('2022-11-20 08:00:00', 11),
                                                                                       ('2022-11-21 06:00:00', 12),
                                                          ('2022-11-22 08:00:00', 11),
                                                          ('2022-11-23 09:00:00', 17),
                                                          ('2022-11-24 08:00:00', 11),
                                                           ('2022-12-1 08:00:00', 11),
                                                           ('2022-12-2 08:00:00', 11),
                                                           ('2022-12-3 09:00:00', 17),
                                                           ('2022-12-4 08:00:00', 11),
                                                                                        ('2022-12-11 08:00:00', 11),
                                                                                        ('2022-12-12 08:00:00', 11),
                                                                                        ('2022-12-13 09:00:00', 17),
                                                                                        ('2022-12-14 08:00:00', 11);


INSERT INTO levelogger(datetime, levelInMeters)
VALUES 
('2020-01-01 06:00:00', 6),
('2021-02-02 06:00:00', 6),
('2021-04-03 07:00:00', 10),
('2022-06-04 08:00:00', 12),
('2022-07-05 09:00:00', 17),
('2022-08-06 06:00:00', 12),
                            ('2022-09-01 06:00:00', 6),
                            ('2022-09-02 06:00:00', 6),
                            ('2022-09-03 07:00:00', 10),
                            ('2022-09-04 08:00:00', 12),
                            ('2022-09-05 09:00:00', 17),
                            ('2022-09-06 06:00:00', 12),
                            ('2022-09-07 06:00:00', 6),
                            ('2022-09-08 06:00:00', 6),
                            ('2022-09-09 07:00:00', 10),
                            ('2022-09-10 08:00:00', 12),
                            ('2022-09-11 09:00:00', 17),
                            ('2022-09-12 06:00:00', 12),
                            ('2022-09-13 08:00:00', 13),
                            ('2022-09-14 07:00:00', 9),
                            ('2022-09-15 08:00:00', 11),
                            ('2022-09-16 09:00:00', 17),
                            ('2022-09-17 06:00:00', 6),
                            ('2022-09-18 06:00:00', 6),
                            ('2022-09-19 07:00:00', 10),
                            ('2022-09-20 08:00:00', 12),
                            ('2022-09-21 09:00:00', 17),
                            ('2022-09-22 06:00:00', 12),
                            ('2022-09-23 06:00:00', 6),
                            ('2022-09-24 06:00:00', 6),
                            ('2022-09-25 07:00:00', 10),
                            ('2022-09-26 08:00:00', 12),
                            ('2022-09-27 09:00:00', 17),
                            ('2022-09-28 06:00:00', 12),
                            ('2022-09-29 08:00:00', 13),
                            ('2022-09-30 07:00:00', 9),
                            ('2022-10-01 08:00:00', 11),
                                                        ('2022-10-02 09:00:00', 17),
                                                        ('2022-10-02 08:00:00', 11),
                                                        ('2022-10-03 09:00:00', 17),
                                                        ('2022-10-04 08:00:00', 11),
                                                        ('2022-10-05 09:00:00', 17),
                                                        ('2022-10-06 08:00:00', 11),
                                                        ('2022-10-07 09:00:00', 17),
                                                        ('2022-10-08 08:00:00', 11),
                                                        ('2022-10-09 09:00:00', 17),
                                                        ('2022-10-10 08:00:00', 11),
                                                        ('2022-10-11 09:00:00', 17),
                                                        ('2022-10-12 08:00:00', 11),
                                                        ('2022-10-13 09:00:00', 17),
                                                        ('2022-10-14 08:00:00', 11),
                                                        ('2022-10-15 09:00:00', 17),
                                                        ('2022-10-16 08:00:00', 11),
                                                        ('2022-10-17 09:00:00', 17),
                                                        ('2022-10-18 08:00:00', 11),
                                                        ('2022-10-19 09:00:00', 17),
                                                        ('2022-10-20 08:00:00', 11),
                                                        ('2022-10-21 06:00:00', 12),
                                                                                       ('2022-11-01 08:00:00', 11),
                                                                                       ('2022-11-02 09:00:00', 17),
                                                                                       ('2022-11-02 08:00:00', 11),
                                                                                       ('2022-11-03 09:00:00', 17),
                                                                                       ('2022-11-04 08:00:00', 11),
                                                                                       ('2022-11-05 09:00:00', 17),
                                                                                       ('2022-11-06 08:00:00', 11),
                                                                                       ('2022-11-07 09:00:00', 17),
                                                                                       ('2022-11-08 08:00:00', 11),
                                                                                       ('2022-11-09 09:00:00', 17),
                                                                                       ('2022-11-10 08:00:00', 11),
                                                                                       ('2022-11-11 09:00:00', 17),
                                                                                       ('2022-11-12 08:00:00', 11),
                                                                                       ('2022-11-13 09:00:00', 17),
                                                                                       ('2022-11-14 08:00:00', 11),
                                                                                       ('2022-11-15 09:00:00', 17),
                                                                                       ('2022-11-16 08:00:00', 11),
                                                                                       ('2022-11-17 09:00:00', 17),
                                                                                       ('2022-11-18 08:00:00', 11),
                                                                                       ('2022-11-19 09:00:00', 17),
                                                                                       ('2022-11-20 08:00:00', 11),
                                                                                       ('2022-11-21 06:00:00', 12),
                                                           ('2022-11-22 08:00:00', 11),
                                                           ('2022-11-23 09:00:00', 17),
                                                           ('2022-12-1 08:00:00', 11),
                                                           ('2022-12-2 08:00:00', 11),
                                                           ('2022-12-3 09:00:00', 17),
                                                           ('2022-12-4 08:00:00', 11),
                                                                                        ('2022-12-11 08:00:00', 11),
                                                                                        ('2022-12-12 08:00:00', 11),
                                                                                        ('2022-12-13 09:00:00', 17),
                                                                                        ('2022-12-14 08:00:00', 11);
