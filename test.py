# -*- coding: utf-8 -*-
from textblob import TextBlob


def get_sent_analy(text):
	blob = TextBlob(text)
	total_score = 0;
	for sentence in blob.sentences:
		total_score+=sentence.sentiment.polarity
	return total_score

if __name__ == '__main__':
	text = "In Japan, strange creatures that eat humans are around and they\"re called \"Ghoul\". A university student, Kaneki Ken, is riding a normal life and has fallen in love with a girl. But, after their first date it turns out that she's a Ghoul. Being seriously traumatized, he got saved as the Ghoul accidentally died."
	tg = get_sent_analy(text)
	print("Tokyo ghoul: "+str(tg))
	s = "Yukihira Souma's dream is to become a full-time chef in his father's restaurant and surpass his father's culinary skill. But just as Yukihira graduates from middle schools his father, Yukihira Jouichirou, closes down the restaurant to cook in Europe. Although downtrodden, Souma's fighting spirit is rekindled by a challenge from Jouichirou which is to survive in an elite culinary school where only 10% of the students graduate. Can Souma survive?"
	s_s = get_sent_analy(s)
	print("shokugeki: "+str(s_s))
	m = ("Monsters they're real, and they want to date us! Three years ago, the world learned that harpies, centaurs, catgirls, and all manners of fabulous creatures are not merely fiction; they are flesh and blood not to mention scale, feather, horn, and fang. Thanks to the \"Cultural Exchange Between Species Act,\" these once mythical creatures have assimilated into society, or at least, they're trying.When a hapless human named Kurusu Kimihito is inducted as a \"volunteer\" into the government exchange program, his world is turned upside down. A snake like lamia named Miia comes to live with him, and it is Kurusu's job to take care of her and make sure she integrates into his everyday life. Unfortunately for Kurusu, Miia is undeniably sexy, and the law against interspecies breeding is very strict. Even worse, when a ravishing centaur girl and a flirtatious harpy move in, what's a full blooded young man with raging hormones to do").encode('utf-8')
	m_s = get_sent_analy(m)
	print("monster girls: "+str(m_s))
	f = "Fate/Zero takes place 10 years prior to the events of Fate/stay night, detailing the events of the 4th Holy Grail War in Fuyuki City. The War of the Holy Grail is a contest in which seven magi summon seven Heroic Spirits to compete to obtain the power of the \"Holy Grail,\" which grants a miracle. After three inconclusive wars for the elusive Holy Grail, the Fourth War commences.Founded by the Einzbern, Makiri, and Tohsaka families centuries ago, the Einzbern family is determined to achieve success after three successive failures, no matter the cost. As a result, they have elected to bring the hated magus killer, Kiritsugu Emiya, into their ranks, despite his methods and reputation as a skilled mercenary and a hitman who employs whatever he can use to accomplish his goals. Though Kiritsugu had once wanted to become a hero who could save everyone, he has long since abandoned this ideal upon realizing that saving one person comes at the cost of another's life. For the sake of humanity, he will ruthlessly destroy anything and anyone who threatens the peace of others. However, Kiritsugu finds himself deeply torn between the love he has found for his new family his wife Irisviel and their daughter Illya and what he must do to obtain the Holy Grail. Meanwhile, Kiritsugu's greatest opponent appears in the form of Kirei Kotomine, a priest who cannot find any sense of fulfillment in his life and sets his sights on Kiritsugu as the possible answer to the emptiness he feels."
	f_s = get_sent_analy(f)
	print("fate\zero: "+str(f_s))