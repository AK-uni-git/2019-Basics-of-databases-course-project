INSERT INTO "Video" ("Nimi", "Tiedostopolku", "Kesto") VALUES ('Lomavideo 2001', 'C:\Videot', '02:15:00');
INSERT INTO "Video" ("Nimi", "Tiedostopolku", "Kesto") VALUES ('Mökkivideo 1998', 'C:\Videot', '01:30:00');
INSERT INTO "Video" ("Nimi", "Tiedostopolku", "Kesto") VALUES ('Kesä 1999', 'C:\Videot', '03:00:00');


INSERT INTO  "Ajankohta" ("Nimi", "Pvm", "Alku", "Loppu") VALUES ('Mummola', '2001-04-28', '01:09:30', '01:30:43');
INSERT INTO  "Ajankohta" ("Nimi", "Pvm", "Alku", "Loppu") VALUES ('Helsinki', '2001-04-29', '01:45:38', '01:59:53');

INSERT INTO  "Ajankohta" ("Nimi", "Pvm", "Alku", "Loppu") VALUES ('Uinti', '1998-06-29', '00:24:38', '00:33:33');
INSERT INTO  "Ajankohta" ("Nimi", "Pvm", "Alku", "Loppu") VALUES ('Nikkarointi', '1998-07-13', '01:34:28', '01:55:33');


INSERT INTO  "Ajankohta" ("Nimi", "Pvm", "Alku", "Loppu") VALUES ('Kalastus', '1999-07-08', '00:32:28', '00:45:23');
INSERT INTO  "Ajankohta" ("Nimi", "Pvm", "Alku", "Loppu") VALUES ('Uinti', '1999-07-12', '01:24:38', '00:33:33');
INSERT INTO  "Ajankohta" ("Nimi", "Pvm", "Alku", "Loppu") VALUES ('Saunanrakennus', '1999-07-15', '01:37:28', '01:58:33');




INSERT INTO  "Postinumero" ("Kaupunki", "Numero") VALUES ('Helsinki', '00120');
INSERT INTO  "Postinumero" ("Kaupunki", "Numero") VALUES ('Tuusula', '04330');
INSERT INTO  "Postinumero" ("Kaupunki", "Numero") VALUES ('Iitti', '47520');


INSERT INTO  "Osoite" ("Katu", "Maa", "PostID") VALUES ('Katajankuja 10 B 17', 'Suomi', 2);
INSERT INTO  "Osoite" ("Katu", "Maa", "PostID") VALUES ('PekonPolku 8', 'Suomi', 2);
INSERT INTO  "Osoite" ("Katu", "Maa", "PostID") VALUES ('Porvarikatu 2 A 11', 'Suomi', 1);
INSERT INTO  "Osoite" ("Katu", "Maa", "PostID") VALUES ('Edustajantie 4', 'Suomi', 1);
INSERT INTO  "Osoite" ("Katu", "Maa", "PostID") VALUES ('Lyöttiläntie 77', 'Suomi', 3);



INSERT INTO  "Henkilo" ("OsoiteID", "Etunimi", "Sukunimi", "Synt_aika") VALUES (1, 'Janne', 'Sormunen', '1987-02-25');
INSERT INTO  "Henkilo" ("OsoiteID", "Etunimi", "Sukunimi", "Synt_aika") VALUES (1, 'Sirpa', 'Sormunen', '1988-06-13');

INSERT INTO  "Henkilo" ("OsoiteID", "Etunimi", "Sukunimi", "Synt_aika") VALUES (2, 'Aatos', 'Isotalo', '1967-08-02');

INSERT INTO  "Henkilo" ("OsoiteID", "Etunimi", "Sukunimi", "Synt_aika") VALUES (3, 'Merja', 'Neuvonen', '1972-10-22');

INSERT INTO  "Henkilo" ("Etunimi", "Sukunimi", "Synt_aika") VALUES ('Erkki', 'Koditon', '1975-09-18');


INSERT INTO "Paikka" ("OsoiteID", "Nimi") VALUES (5, 'Mökki');
INSERT INTO "Paikka" ("OsoiteID", "Nimi") VALUES (4, 'Johanneksen Kirkko');
INSERT INTO "Paikka" ("OsoiteID", "Nimi") VALUES (1, 'Koti');


INSERT INTO "VideonAjankohta" ("VideoID", "AjankohtaID") VALUES (1, 1);
INSERT INTO "VideonAjankohta" ("VideoID", "AjankohtaID") VALUES (1, 2);
INSERT INTO "VideonAjankohta" ("VideoID", "AjankohtaID") VALUES (2, 3);
INSERT INTO "VideonAjankohta" ("VideoID", "AjankohtaID") VALUES (2, 4);
INSERT INTO "VideonAjankohta" ("VideoID", "AjankohtaID") VALUES (3, 5);
INSERT INTO "VideonAjankohta" ("VideoID", "AjankohtaID") VALUES (3, 6);
INSERT INTO "VideonAjankohta" ("VideoID", "AjankohtaID") VALUES (3, 7);


INSERT INTO "AjankohdanP" ("AjankohtaID", "PaikkaID") VALUES (2,2);
INSERT INTO "AjankohdanP" ("AjankohtaID", "PaikkaID") VALUES (3,1);
INSERT INTO "AjankohdanP" ("AjankohtaID", "PaikkaID") VALUES (4,1);
INSERT INTO "AjankohdanP" ("AjankohtaID", "PaikkaID") VALUES (5,1);   
INSERT INTO "AjankohdanP" ("AjankohtaID", "PaikkaID") VALUES (6,3); 


INSERT INTO "AjankohdanH" ("AjankohtaID", "HenkiloID") VALUES (1,1);
INSERT INTO "AjankohdanH" ("AjankohtaID", "HenkiloID") VALUES (1,2);  
INSERT INTO "AjankohdanH" ("AjankohtaID", "HenkiloID") VALUES (2,3); 
INSERT INTO "AjankohdanH" ("AjankohtaID", "HenkiloID") VALUES (3,3); 
INSERT INTO "AjankohdanH" ("AjankohtaID", "HenkiloID") VALUES (4,3); 
INSERT INTO "AjankohdanH" ("AjankohtaID", "HenkiloID") VALUES (5,3); 
INSERT INTO "AjankohdanH" ("AjankohtaID", "HenkiloID") VALUES (6,4);
INSERT INTO "AjankohdanH" ("AjankohtaID", "HenkiloID") VALUES (6,2);
INSERT INTO "AjankohdanH" ("AjankohtaID", "HenkiloID") VALUES (6,1);
INSERT INTO "AjankohdanH" ("AjankohtaID", "HenkiloID") VALUES (7,3);  