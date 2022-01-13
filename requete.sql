SELECT User.last_name, User.first_name, Entreprise.place, Candidature.contact 
FROM Candidature, User, Entreprise
WHERE User.id = Candidature.user_id 
AND Candidature.enterprise_id = (Select id 
                                FROM Entreprise
                                WHERE LOWER(name) = 'urluberlu')