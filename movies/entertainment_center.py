import fresh_tomatoes
import media


Spider_Man_Homecoming = media.Movie("Spider-Man", "Thrilled by his experience with the Avengers, young Peter Parker returns home to live with his Aunt May. Under the watchful eye of mentor Tony Stark, Parker starts to embrace his newfound identity as Spider-Man. He also tries to return to his normal daily routine -- distracted by thoughts of proving himself to be more than just a friendly neighborhood superhero. Peter must soon put his powers to the test when the evil Vulture emerges to threaten everything that he holds dear.", "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg", "https://www.youtube.com/watch?v=rk-dF1lIbIg")

Deadpool_2 = media.Movie("Deadpool 2", "Wisecracking mercenary Deadpool joins forces with three mutants -- Bedlam, Shatterstar and Domino -- to protect a boy from the all-powerful Cable.", "http://t2.gstatic.com/images?q=tbn:ANd9GcTkbXNbwGV0npOKCGSndE-YCGpRb2xQDRV8VyMfGlsEfej-sVMv", "https://www.youtube.com/watch?v=D86RtevtfrA")

Ant_Man_and_The_Wasp = media.Movie("Ant-Man and The Wasp", " Real heroes. Not actual size. Marvel Studios' Ant-Man and The Wasp is In theaters July 6","http://t1.gstatic.com/images?q=tbn:ANd9GcQeA9IA-C1GiNpVwEXXm-jcFOFpuYvjd-n30RmAtSs8511N2NMi","https://www.youtube.com/watch?v=UUkn-enk2RU")

Avengers = media.Movie("Avengers" , "When Thor's evil brother, Loki, gains access to the unlimited power of the energy cube called the Tesseract, Nick Fury, director of S.H.I.E.L.D., initiates a superhero recruitment effort to defeat the unprecedented threat to Earth. Joining Fury's 'dream' team are Iron Man , Captain America , the Hulk, Thor, the Black Widow and Hawkeye.", "http://t1.gstatic.com/images?q=tbn:ANd9GcTp0qlAoWcOOswIkL_qpjYzJqCCDmWXiBzCXiqbE43Obo8c0Z-s", "https://www.youtube.com/watch?v=eOrNdBpGMv8")

Avengers_Age_of_Ultron = media.Movie("Avengers Age of Ultron", "When Tony Stark jump-starts a dormant peacekeeping program, things go terribly awry, forcing him, Thor, the Incredible Hulk and the rest of the Avengers to reassemble. As the fate of Earth hangs in the balance, the team is put to the ultimate test as they battle Ultron, a technological terror hell-bent on human extinction. Along the way, they encounter two mysterious and powerful newcomers, Pietro and Wanda Maximoff", "http://t0.gstatic.com/images?q=tbn:ANd9GcRlGeugacRkKznDOtRhUCVt0AkrOTPbaaKwF9xgGZgNViyC_Xko", "https://www.youtube.com/watch?v=tmeOjFno6Do")

Avengers_Infinity_War = media.Movie("Avengers Infinity War", "Iron Man, Thor, the Hulk and the rest of the Avengers unite to battle their most powerful enemy yet -- the evil Thanos. On a mission to collect all six Infinity Stones, Thanos plans to use the artifacts to inflict his twisted will on reality. The fate of the planet and existence itself has never been more uncertain as everything the Avengers have fought for has led up to this moment", "https://images-na.ssl-images-amazon.com/images/I/A1t8xCe9jwL._SY679_.jpg" ,"https://www.youtube.com/watch?v=6ZfuNTqbHE8")


movies = [ Spider_Man_Homecoming, Deadpool_2, Ant_Man_and_The_Wasp, Avengers, Avengers_Age_of_Ultron , Avengers_Infinity_War]

fresh_tomatoes.open_movies_page(movies)











