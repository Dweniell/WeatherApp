SELECT p.Locatie,p.First_Name,p.Last_Name,v.quality FROM votes v,persons p WHERE v.chosen_person = p.id AND v.valid=1;
