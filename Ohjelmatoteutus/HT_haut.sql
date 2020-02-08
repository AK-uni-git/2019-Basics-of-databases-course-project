-- Listaa kaikkien videoiden tiedot
SELECT * FROM "Video";

-- Listaa videoiden kaikki ajankohdat
SELECT "Video"."nimi" AS 'Videon nimi', "Video"."Tiedostopolku", "Video"."Kesto" AS 'Videon kesto',
    "Ajankohta"."Nimi" AS 'Ajankohdan nimi', "Ajankohta"."Pvm", "Ajankohta"."Alku", "Ajankohta"."Loppu"  FROM "Video" 
    INNER JOIN "VideonAjankohta" ON "VideonAjankohta"."VideoID" = "Video"."VideoID"
    INNER JOIN "Ajankohta" ON "Ajankohta"."AjankohtaID" = "VideonAjankohta"."AjankohtaID";

-- Listaa henkilöiden osoitteet
SELECT "Henkilo"."Etunimi", "Henkilo"."Sukunimi", "Osoite"."Katu" AS 'Katuosoite',
    "Postinumero"."Kaupunki", "Postinumero"."Numero" AS 'Postinumero', "Osoite"."Maa" FROM "Henkilo"
    LEFT OUTER JOIN "Osoite" ON "Henkilo"."OsoiteID" = "Osoite"."OsoiteID"
    LEFT OUTER JOIN "Postinumero" ON "Osoite"."PostID" = "Postinumero"."PostID";

-- Etsi kaikki ajankohdat tietyn paikan mukaan
SELECT "Paikka"."Nimi" AS 'Paikan nimi', 'on ajankohdassa' AS "Selite 1",
    "Ajankohta"."Nimi" AS 'Ajankohdan nimi', "Ajankohta"."Pvm", "Ajankohta"."Alku", "Ajankohta"."Loppu"  FROM "Ajankohta" 
    INNER JOIN "AjankohdanP" ON "Ajankohta"."AjankohtaID" = "AjankohdanP"."AjankohtaID"
    INNER JOIN "Paikka" ON "AjankohdanP"."PaikkaID" = "paikka"."PaikkaID"
    WHERE "Paikka"."Nimi" = ?;

-- Etsi kaikki ajankohdat tietyn henkilön mukaan
SELECT "Henkilo"."Etunimi", "Henkilo"."sukunimi", 'on ajankohdassa' AS "Selite 1",
    "Ajankohta"."Nimi" AS 'Ajankohdan nimi', "Ajankohta"."Pvm", "Ajankohta"."Alku", "Ajankohta"."Loppu"  FROM "Ajankohta" 
    INNER JOIN "AjankohdanH" ON "Ajankohta"."AjankohtaID" = "AjankohdanH"."AjankohtaID"
    INNER JOIN "Henkilo" ON "AjankohdanH"."HenkiloID" = "Henkilo"."HenkiloID"
    WHERE "Henkilo"."Etunimi" = ? AND "Henkilo"."sukunimi" = ? ;

-- Muokkaa henkilön tietoja
UPDATE "Henkilo" SET
   "OsoiteID" = ?, "Etunimi" = ?, "Sukunimi" = ?, "Synt_aika" = ?
   WHERE "Etunimi" = ? AND "Sukunimi" = ?;
   -- Bonushaku, joka näytetään päivityksen jälkeen uusien tietojen varmistamiseksi:
    SELECT * FROM "Henkilo"
    WHERE "Etunimi" = ? AND "Sukunimi" = ?;

-- Lisää uusi video
INSERT INTO "Video" ("Nimi", "Tiedostopolku", "Kesto") VALUES (?, ?, ?);

-- Luo videon ajankohtien määrästä kuvaaja
SELECT "Video"."Nimi" AS 'Videon nimi', COUNT ("Ajankohta") AS 'Ajankohtia' FROM "Video" 
    INNER JOIN "VideonAjankohta" ON "VideonAjankohta"."VideoID" = "Video"."VideoID"
    INNER JOIN "Ajankohta" ON "Ajankohta"."AjankohtaID" = "VideonAjankohta"."AjankohtaID"
    GROUP BY "Video"."VideoID";