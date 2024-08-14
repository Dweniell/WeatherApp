SELECT p.Locatie,count(v.id) as votes from persons p left join votes v on p.id = v.chosen_person and v.valid=1 group by p.Locatie;
