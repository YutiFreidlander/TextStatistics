# TextStatistics

This program get a text file wich contains English text.
The program analyses the text, and print some information.
For this program I used the NLTK library of Python, for analyze the natural language.
For find the characters names I analyzed the POS of the sentences.

For example, I tested the program on this text file:
https://github.com/kzjeef/algs4/blob/master/burrowswheelers/testfile/dickens.txt

The results:

1. Lines count: 84583

2. Words count: 760339

3. Unique words count: 9206

4.1. Words AVG in sentence: 8.989264982325054

4.2. Longest sentence:  

    When I first peeped in at
    the gate of the lifeless quadrangle, and started from the
    mouldering statue becoming visible to me like its guardian ghost;
    when I stole round by the back of the farm-house, and got in among
    the ancient rooms, many of them with their floors and ceilings
    falling, the beams and rafters hanging dangerously down, the
    plaster dropping as I trod, the oaken panels stripped away, the
    windows half walled up, half broken; when I discovered a gallery
    commanding the old kitchen, and looked down between balustrades
    upon a massive old table and benches, fearing to see I know not
    what dead-alive creatures come in and seat themselves, and look up
    with I know not what dreadful eyes, or lack of eyes, at me; when
    all over the house I was awed by gaps and chinks where the sky
    stared sorrowfully at me, where the birds passed, and the ivy
    rustled, and the stains of winter weather blotched the rotten
    floors; when down at the bottom of dark pits of staircase, into
    which the stairs had sunk, green leaves trembled, butterflies
    fluttered, and bees hummed in and out through the broken door-ways;
    when encircling the whole ruin were sweet scents, and sights of
    fresh green growth, and ever-renewing life, that I had never
    dreamed of, - I say, when I passed into such clouded perception of
    these things as my dark soul could compass, what did I know then of
    Hoghton Towers?
    
    
5.1. Most popular word: [('the', 38410)]

5.2. Most popular word exclude stop words: [('said', 4253)]

6. Longest word sequence without 'k' words:   

    herself, would have been
    prostration, and that she would have fallen, in point of fact, a
    victim.'

    'Now, Dombey! - ' says the Major, resuming his discourse with great
    energy.

    'I beg your pardon,' interposes Cousin Feenix. 'Allow me another
    word. My friend Dombey will permit me to say, that if any circumstance
    could have added to the most infernal state of pain in which I find
    myself on this occasion, it would be the natural amazement of the
    world at my lovely and accomplished relative (as I must still beg
    leave to call her) being supposed to have so committed herself with a
    person - man with white teeth, in point of fact - of very inferior
    station to her husband. But while I must, rather peremptorily, request
    my friend Dombey not to criminate my lovely and accomplished relative
    until her criminality is perfectly established, I beg to assure my
    friend Dombey that the family I represent, and which is now almost
    extinct (devilish sad reflection for a man), will interpose no
    obstacle in his way, and will be happy to assent to any honourable
    course of proceeding, with a view to the future, that he may point
    out. I trust my friend Dombey will give me credit for the intentions
    by which I am animated in this very melancholy affair, and - a - in
    point of fact, I am not aware that I need trouble my friend Dombey
    with any further observations.'

    Mr Dombey bows, without raising his eyes, and is silent.

    'Now, Dombey,' says the Major, 'our friend Feenix having, with an
    amount of eloquence that Old Joe B. has never heard surpassed - no, by
    the Lord, Sir! never!' - says the Major, very blue, indeed, and
    grasping his cane in the middle - 'stated the case as regards the
    lady, I shall presume upon our friendship, Dombey, to offer a word on
    another aspect of it. Sir,' says the Major, with the horse's cough,
    'the world in these things has opinions, which must be satisfied.'

    'I
      
7. Biggest number:   twenty million 

8. Colors:  
    
    dict_items([('black', 258), ('white', 183), ('red', 184), ('yellow', 28), ('brown', 45), ('blue', 111), ('green', 77), ('silver', 38), ('gold', 53), ('purple', 13), ('orange', 5), ('pink', 5), ('gray', 10)])

9.1. Names: 
    
    {'Bill Bitherstone', 'Stephen', 'Halloa', 'Dover', 'Master Barnet', 'Long', 'Thou', 'Loose', 'Mr. Silverman', 'Monsieur Defarge', 'Robert', 'Quebec', 'George Goff', 'Great', 'Transcendentalism', 'Stryver', 'Memory', 'Shaker Village', 'Mrs Baps', 'Macbeth', 'Woe', 'Temple Bar', 'Grunt', 'Character Beneath', 'Adelina', 'Joey B', 'Robby', 'Jane', 'Heavens', 'Lake Champlain', 'Walker', 'Josh', 'Jacques', 'Pitt', 'Yonder', 'Success', 'Emma Gordon', 'Captain Sherman', 'Major Allison', 'Bayswater', 'Miss Pipson', 'Miss Bule', 'Afraid', 'Taste', 'Young Toots', 'Alexander', 'Guilty', 'Hartford', 'Gardens', 'Trimmer', 'Essay', 'Mr. Stryver', 'Jacques Four', 'Gradgrinds', 'Major Gally', 'Samuel Thurston', 'Mills', 'Northward', 'Joseph Gradgrind', 'Parnassus', 'Walter Gay', 'Show Concord', 'Howe', 'Johnny Cake', 'Rachael', 'Earth', 'Well', 'Yorick', 'John Bunsby', 'Simple', 'Childerth', 'Henry', 'Drawn', 'Jim Blake', 'Martyrdom', 'Stop', 'Blackpot', 'Mr. P. Arpin', 'Mr. Swidger', 'Domber', 'Mr. Cruncher', 'Gorgon', 'Miss Josephine Sleary', 'Boy', 'Noah', 'Line', 'Universal Distrust', 'Cheerless', 'Patriots', 'Citizen Doctor', 'Wiggs', 'Rumour', 'Master Skettles', 'Birth', 'Close', 'Antoine', 'Jane Gradgrind', 'Dombei', 'Louis Fifteen', 'Nature', 'Lessons', 'Thick', 'Laura Bridgman', 'Great Britain', 'Honest Captain Cuttle', 'Alfred Starling', 'Billy Joper', 'Hoofs', 'Citizen Gabelle', 'Quickly', 'Mount', 'Boys', 'Sir Barnet Skettles', 'Driven', 'Anna Dominoes', 'Monseigneur', 'Defoe', 'Luckily', 'Joe Dennis', 'Ikey', 'Captain', 'Later Tellson', 'Lady Scadgers', 'Miss Pankey', 'Old Stephen', 'Caddo Gazette', 'Wisdom', 'Cave', 'Bartlemy Fair', 'John', 'Mr. Verity Hawkyard', 'Miss Griffin', 'Dark', 'Soon', 'Chancery', 'Toodles', 'Walks', 'Clown', 'Doctor Crocus', 'Mrs Richards', 'Lengths', 'Ease', 'Mr. Childers', 'John Bunyan', 'Miss Toxin', 'Man', 'Tush', 'Shakspeare', 'Benton', 'Upper Sandusky', 'Granville', 'Thank GOD', 'Nearer', 'Glubb', 'Stand', "'Well", 'Think', 'Minerva', 'Dotnbey', 'Redlaw', 'Edith', 'Lucie Darnay', 'Doctor Blimber', 'Joseph Bagstock', 'Otherwise', 'Alpha', 'Heavily', 'Jack Governor', 'Hotel', 'Joseph', 'Joey', 'Bismillah', 'Twenty Pounds', 'Mr. Lorry', 'Look', 'Temperance', 'London Bridge', 'Christian', 'Brother Gimblet', 'Ally', 'Lombard Street', 'Dinner Hall', 'Mr. Robbins', 'Quite', 'Dickson', 'Mr. Charles Darnay', 'Noise', 'Queen', 'Towlinson', 'York', 'Mrs Staggs', 'Poor Mr Toots', 'Right', 'Married', 'Richards', 'Cincinnatus', 'Williams', 'Rapped', 'Sainte Guillotine', 'Master Cruncher', 'Deptford', 'Miss Tox', 'Saint Antoine', 'Dombeys', 'Unless', 'Grinder', 'Angel', 'Shaken', 'Lord Chesterfield', 'Paul Dombey', 'Scott', 'Quiet', 'Delight', 'Physician', "God A'mighty", 'Months', 'Arpin', 'Jury', 'George Gradgrind', 'Owners', "Haply 't", 'Preston', 'Master Paul', 'Bearin', 'Syd', 'Mama', 'Scorn', 'Bed', 'Solomon John', 'Gas', 'Fawkes', 'Madison', 'John Gradgrind', 'La Guillotine', 'Hurry', 'Reid', 'Aged', 'Mr. Crunches', 'Behave', 'Father Mathew', 'Gaspard', 'Jack Adams', 'Help', 'Happy Florence', 'Sleary', 'Galileo', 'Husbands', 'Gratitude', 'Brandy', 'Poor Carton', 'Kentucky Tom', 'Graves', 'Harvey', 'Summer', 'Prison Discipline', 'Isaac', 'Tommy Screwzer', 'Randal', 'Lord Feenix', 'Calm', 'Hilary', 'Romuluses', 'Coop', 'Young Barnet', 'Izaak Walton', 'Tiddler', 'Tozer', 'Providence', 'Alexandre Manette', 'Speak', 'Freedom', 'Care', 'Mr. Jerry Cruncher', 'Poor', 'Black', 'Sharkey', 'Harriet Carker', 'Thank Heaven', 'Parker Peps', 'Strange News', 'Old Bailey Spi', 'Diedrich Knickerbocker', 'Obey', 'Wild', 'Buggins', 'Nowt', 'Joe Bagstock', 'Guy Fawkes', 'Adieu', 'Mr. Granville Wharton', 'Missus', 'John Milton', 'Master B', 'Hay', 'Vixen', 'Willingly', 'Midnight Murder', 'Church', 'Bryanstone Square', 'Bench Bar', 'Mr. Chadwick', 'Stone Lodge', 'Anon', 'Pan', 'Queenston', 'Gillespie', 'Grand Vizier', 'Brother John', 'Mariner Time', 'Boz', 'Baby', 'Thingummy', 'Son', 'Mr. Greenough', 'Whereas', 'Curious', 'Shooter', 'Ground', 'Lewis', 'Charles Evremonde', 'Greater', 'Witness Cousin Feenix', 'Faith', 'Cleopatra', 'Benjamin', 'School', 'Classes', 'Creation', 'Passion', 'Slight', 'Daughter', 'Montreal', 'Magsman', 'Cross', 'Wild Ass', 'Captain Cutlle', 'Wolf', 'Emma', 'Messenger', 'Mark Lane', 'Harlequin', 'Harriet', 'Jacques Five', 'Old Sol', 'Breakfast', 'Jaundiced Jail', 'Patty', 'Liggs', 'Air', 'James Cottingham', 'Sardana', 'Round', 'Lewiston', 'Champagne', 'Wait', 'Peg', 'Deep', 'Anxious', 'Camden Town', 'Sissy', 'Say', 'Toby Magsman', 'JOHN', 'Public', 'Stick', 'Slowly', 'Great Heaven', 'Samson', 'Hell Gate', 'Miss Dombey', 'Phenomenon', 'Kidderminthter', 'Facts', 'Walter Gay Walter', 'Pantheon', 'Mary Queen', 'Charley Swidger', 'Hence Monseigneur', 'Giddiness', 'John Carker', 'Bunsby', 'Seen', 'Bloody Island', 'Kenilworth', 'Hot', 'Doe', 'Cicero', 'Florence Dombey', 'Toby', 'William', 'Slavery', 'Madge Wildfire', 'Saint Antoine Quarter', 'Lady Fareway', 'Tommy', 'Fool', 'East India', 'Johnny Tetterby', 'Burgess', 'Bounderby', 'Little Rifle', 'William Hine', 'Licker', 'Babylon', 'Leonora', 'Mr. Harthouse', 'Seltzer', 'Balls Pond', 'Mr. Fareway', 'Cheer', 'Change', 'Peace', 'Mr. Carton', 'Harris', 'Rend Foulon', 'Rule Britannia', 'Cruncher', 'Laughter', 'Major Gillespie', 'Bright', 'Pull', 'Captain Cuttle', 'Hurrah', 'Wolfe', 'Castlereagh', 'Medusa', 'STRAW HAT', 'Biler', 'Jarber', 'Crypt', 'Liberty', 'Poor Justice', 'Schools', 'Josephine', 'Mound', 'Gay', 'Monsieur Paris', 'Mr. Arndt', 'Barnum', 'Monsieur', 'Debt', 'Griffin', 'Guard', 'Chaney', 'Tabby', 'Anno Domini', 'Potter', 'Clark', 'Mother', 'John Herschel', 'Dim', 'Mariner', 'Columbus', 'Therry', 'Solomon Pross', 'Porter', 'Michaelmas Term', 'Edward Cuttle', 'Englishman', 'Dennis', 'Charles MacStinger', 'Mind', 'Clock Room', 'Wisconsin', 'Perch', 'Alice', 'Free', 'George Washington', 'Latin', 'Paul Jones', 'J. Bagstock', 'Miss Floy', 'Foulon', 'Josh Bagstock', 'Jacques One', 'Write', 'Grace', 'Quarter Sessions', 'Seven Dials', 'Brave', 'Coketowner', 'Sam', 'Giant', 'John Solomon', 'Major', 'Dutchman', 'Equally', 'Royal', 'Thleary', 'Sandusky', 'Miss Florence', 'Warbler', 'Hastily', 'Fame', 'Brother', 'Noakes', 'Young Thomas', 'Cassim Baba', 'Life', 'Bad Fortune', 'Publicly', 'Brother Parksop', 'Briggs', 'Sol Gills', 'Walter', 'Virgil', "Mrs Dombey's", 'Run', 'Sad', 'Bill', 'Martyr', 'Mr. Beaver', 'Food', 'Single', 'Bury', 'Persons', 'Pond', 'Remus', 'Nipper', 'Old', 'Susan', 'Sir', 'Miss Pross', 'Heart', 'Danger', 'Mrs Chic', 'Paralysis', 'Dowager', 'Ally Loo', 'Cuttle', 'Hooroar', 'Shake', 'Doctor Parker Pep', 'Chiefly Matrimonial', 'Banks', 'Damp', 'Miss Bounderby', 'Judas Iscariot', 'Captain Gills', 'Mr. William Button', 'Steady', 'Rather', 'Pegler', 'Robbed', 'Louisa Chick', 'Wife', 'Mrs Blimber', 'Jackson', 'Apples', 'Blacksmith', 'Lowell', 'Parker', 'Brother Hawkyard', 'Grundy', 'Clean', 'Vagabond', 'Tilson', 'Limited', 'Cook', 'Abudah', 'Mrs Bokum', 'Uncle', 'Somewhere', 'Woman', 'Unbidden', 'Books', 'Whether Bunsby', 'Mouse', 'Framed', 'Mystery', 'Within', 'Wi', 'Beyond', 'Torn Gradgrind', 'Temperance Songs', 'Shawnees', 'Miss Fareway', 'Oliver Caswell', 'Tom', 'Mother Bunch', 'Miff', 'Objects', 'Bar', 'Jerry', 'Broadway', 'Sorrow', 'Methought', 'Massachusetts Asylum', 'Madame Defarge', 'Homer', 'Mr. Kidderminster', 'Grown', 'Little Paul', 'Loo Gradgrind', 'Bird Waltzes', 'Old Joe', 'Aggerawayter', 'Least', 'Miss Nipper', 'James Surgette', 'Mary Tofts', 'Mill', 'Truly', 'Mr. Gradgrind', 'Miss Susan Nipper', 'Poor Paul', 'Heir', 'Witness Major Bagstock', 'Vistors', 'Son Dombey', 'Ology', 'Lucie Manette', 'Adam', 'Sydney', 'Toodle', 'Express', 'Yo', 'Lord Burleigh', 'Misses Brown', 'Strike', 'Strange', 'Marry', 'Timid', 'Young Jerry', 'Cly', 'Nobody', 'Toots', 'La Trappe', 'Unsought', 'Poor Berry', 'Scots', 'Lengthy', 'Lucretia Tox', 'Ships', 'Mr. Harker', 'Lord Nelson', 'God', 'Saint Paul', 'Took', 'Chateau', 'Sheep', 'Pale', 'Kentucky Giant', 'Baps', 'Dickenson', 'Stakes', 'Falsest', 'Queen Victoria', 'French Lewis', 'Never', 'Mr. Willet', 'Warwick', 'Lucie', 'Slackbridge', 'Bah', 'Mr. Redlaw', 'Mary', 'Carton', 'Molten', 'Mr. Robins', 'George Silverman', 'Manuel', 'Rich', 'Mr. Magsman', 'Ogress', 'Chairmen', 'Wales', 'Master Bitherstone', 'Pet', 'Mrs Brown', "'which", 'Jerry Cruncher', 'Master', 'Evremonde', 'Evil', 'Hunger', 'Laura', 'Jack Bunsby', 'Jerusalem', 'Set', 'Immense', 'Better', 'St. Louis', 'Pipchin', 'Old Foulon', 'Mr. Thorn', 'Alcohol', 'Merry', 'Prairie', 'Esquire', 'Impassive', 'Struck', 'Whereupon Doctor Crocus', 'Woodman', 'Pontefract', 'Mr. Cooper', 'Clothes', 'Tox', 'Number One', 'James River', 'Inn', 'Edith Granger', 'Harthouse', 'Tellson', 'Christ', 'Miss Berry', 'Beethoven', 'Robinson', 'Sol', 'Missis', 'Louder', 'Water', 'Mr. James Harthouse', 'Gulliver', 'Hoghton Towers', 'Venus', 'Babel', 'Master Dombey', 'Mr. Catlin', 'Mr. E. S. Baker', 'Bankrupts', 'Robert Potter', 'Mr. Ralph Waldo Emerson', 'Miss', 'Spitfire', 'Turnham Green', 'Cannon', 'Devil', 'Wilful Murder', 'Suspicion', 'Lovely Peg', 'Mister', 'Nine', 'Halifax Harbour', 'Parade', 'Black Hollow', 'Major Bagstock', 'Hereupon', 'Imagine', 'Rhode Island', 'Spy', 'County Ark', 'Crash', 'Lady Jane Finchbury', 'Picture Room', 'Terence', 'Fact', 'Miscreant Foulon', 'Junior', 'Nurse Wickam', 'Manager', 'Mr. Dickens', 'Potomac Creek', 'Alas', 'Shakespeare', 'Tom Gradgrind', 'Mr. Carlyle', 'Happiness', 'Albany', 'Saint Francis Xavier', 'Cecilia Jupe', 'Darwen', 'Something', 'Gimblet', 'Old Mrs Pipchin', 'Smith', 'Barbados', 'Feeder', 'Paris', 'Miss Louisa', 'Joes', 'Legion', 'Dearest Florence', 'Henry James', 'Poor Florence', 'Boldface', 'Merrylegs', 'Shaker', 'V', 'James Carker', 'Rose', 'Jack', 'Good Mrs Brown', 'Whereby', 'Power', 'Hallo', 'Dear Doctor Manette', 'Destiny', 'Place', 'Young Mr. Thomas', 'Funerals', 'John Derrick', 'Gabelle', 'Buffalo', 'Defarge', 'Mrs Pipchin', 'Vitellius', 'Bob', 'Night', 'Baker', 'Niblo', 'Thomas', 'Saint Pancras', 'Papa', 'Bottles', 'James', 'Nephew', 'Ketch', 'Mint', 'Jamaica Harbour', 'Lord Mayor', 'Banker', 'Gooseberry', 'Jem Carker', 'Socrates', 'Johnny Cakes', 'Bless', 'Richard Whittington', 'Queer Street', 'Hoity', 'Louisville', 'Upper Canada', 'Earthly Copper Gallon', 'Family Mansion', 'Try', 'Solomon', 'Matrimonially', 'Lord', 'Josiah Bounderby', 'Coketown Hands', 'Tickle', 'Keys', 'Skettles Junior', 'Robinson Crusoe', 'Villain Foulon', 'Imperious', 'Mr. Undery', 'Jefferson', 'Belleville', 'Native', 'Darnay', 'Carthages', 'Derrick', 'Mr. William Swidger', 'Gad', 'Dinner', 'Fall', 'Vide Poche', 'Blackburn', 'Mrs Dombey', 'Herein', 'Mrs Skewton', 'Warwick Castle', 'Tumbler', 'Believe', 'Romulus', 'Divine Right', 'Niagara', 'Market', 'Sleep', 'Tom Thumb', 'Henceforth', 'Bitherstone', 'Sabbath', 'Might Mr. Harthouse', 'False', 'Grinders', 'Chowley', 'Lorry', 'Maria', 'Hebrew', 'Please', 'Marshal', "Edith 'It", 'Parks', 'Shave', 'Jupiter', 'Martha', 'Bad Mrs Brown', 'Ifs', 'Zobeide', 'Mint Julep', 'Silverman', 'Roar', 'Free Press', 'Lake Ontario', 'Monsieur Gabelle', 'Jamaica', 'Cape Clear', 'Thomas G. Allison', 'Lake Erie', 'Louisa', 'Mr. Granville', "Mr. M'Kane", 'Beast', 'Manchester', 'Bull', 'Dickens', 'Cinderella', 'Brig Place', 'Arabian', 'Fat Ladies', 'Coketown', 'Really', 'Barbados Harbour', 'Light Monsieur', 'Grise', 'Time', 'Folly', 'Miss Tox Lucretia', 'Kirby', 'Mr. Radley', 'Ruins', 'Thomas Gradgrind', 'Damme', 'Papa Teach', 'Old Solomon', 'Carelessly', 'Mr. Darnay', 'Monsieur Orleans', 'Clapham Rise', 'Robin', 'Jarvis Lorry', 'States', 'Lucifer', 'Already', 'Familiar', 'Citizen Evremonde', 'Goodbye', 'Mr. Paap', 'Mr. Webster', 'Midshipman', 'Blot', 'Mrs Wickam', 'Mr. Hart', 'Sir Joseph Bagstock', 'Crush', 'Kate', 'High', 'Jiddy', 'Di', 'Gloomy', 'Denounced', 'Perfect', 'Berinthia', 'Mr. Sparsit', 'Money', 'Miss Harriet', 'Paul', 'Sermuchser', 'Loo', 'Mr. Hawkyard', 'Hell', 'Ross', 'Treason', 'Ladybird', 'Eager', 'Chicken', 'Monsieur Manette', 'Poverty', 'Berry', 'Mr. Barsad', 'Susan Nipper', 'Naturally', 'Turn', "'you", 'Fluffy', 'Carondelet', 'Jim Crows', 'Parksop', 'Whether Miss Tox', 'Dead', 'Good Heaven', 'Blind', 'Poor Briggs', 'Mount Auburn', 'Far', 'Merry Christmas', 'Inside', 'Captain John Bunsby', 'Sabbaths', 'Eas', 'Post Office', 'Always', 'Tom Tiddler', 'Far West', "Mr. Lorry's", 'Antony Bagstock', 'Mrs Miff', 'Chick', 'Pipson', 'Mrs Granger', 'Steam Power', 'Sir Hubert Stanley', 'Echoing Footsteps', 'Ed', 'Almost', 'Beard', 'Bitzer', 'State', 'Public Prosecutor', 'Correct', 'Judy', 'Withers', 'East', 'Whether', 'Yes', 'Dear Carton', 'Pill', 'Betsey Jane', 'Livery', 'Carker', 'Wulturs', 'Spoke', 'Chase', 'Lee', 'Mr. Ross', 'Tea', 'Mr. William', 'Sydney Carton', 'Fresh', 'Piccadilly', 'Saint', 'Mrs Blockitt', 'Sir David Brewster', 'Dombey', 'Old Sol Gills', 'Lovely', 'Peggy', 'Yellow Jack', 'Saint George', 'Bench', 'Cousin Feenix', 'Dwell', 'Madam', 'Rip Van Winkle', 'John Wilburn', 'Spinner', 'Odours', 'Crocus', 'Hands', 'James R. Vinyard', 'Pitcher', 'Mr. Thomas Gradgrind', 'Old Joe Bagstock', 'John Barsad', 'Fancy Ball', 'Reason', 'Stricken', 'Miss Carker', 'Fifty', 'Whether Mr Dombey', 'Signor Jupe', 'Business', 'Poetry', 'Mr. Fall', 'Awake', 'Said Mr. Fareway', 'Gone', 'Busy', 'Street', 'Master Kidderminster', 'Nickits', 'Old Time', 'Fanny', 'Vinyard', 'Sir Richard Whittington', 'Number Three', 'Highly', 'Roman', 'Rachel', 'Fancy', 'Velveteen', 'Le Sage', 'Family', 'Ned Cuttle', 'Three', 'Bankruptcy', 'James Harthouse', 'Lots', 'Bagstock', 'Thomas Gradgrind Esquire', 'Pepper', 'Hope', 'Royalty', 'Everywhere', 'Captain Cuttle Put', 'Sit', 'Major C. Gally', 'Fragile', 'Soda', 'Wal', 'Respectin', 'Jemima', 'Poor Susan', 'Jade', 'Saint Dunstan', 'Shadows', 'Florence', 'Pool', 'Liverpool', 'Shame', 'Billiard Ball', 'Johnson', 'Machinery', 'Midnight', 'Doctor So-and-so', 'Ocean', 'Hilary Term', 'Jacques Three', 'Myra', 'Solomon Gills', 'Jew', "Sir Barnet's", 'Harrisburg', 'Job', 'Streets', 'Majesty', 'Banquet', 'Miss Manette', 'Habeas Corpus', 'Ernest Defarge', 'Timber Doodle', 'Asylum', 'Lady Skettles', 'Pittsburg', 'Mesrour', 'Wally', 'Little Dombey', 'Diogenes', 'Monsieur Charles', 'Bubler', 'Johnny', 'Mount Vernon', 'Hooray', 'Mr. Tom', 'Mrs', 'Miller', 'Arthur', 'Christmas', 'Notre Dame', 'Mrs Chick', 'Punch', 'Reins', 'Towards Soho', 'Boast', '_I_', 'Bravo', 'Brogley', 'De Foe', 'Negress Caroline', 'Thus', 'Dutchmen', 'Famished', 'Sally', 'Bully Stryver', 'Lucretia', 'Poor Fanny', 'John Brown', 'Double Room', 'Whereupon', 'Feenix', 'Hill', 'Powler', 'Miss Lucie', 'Thtick', 'Madeira', 'MR. JAMES', 'Gravesend', 'Mr. Sleary', 'Staggs', 'Alexander MacStinger', 'Cauliflower Act', 'Darkness', 'Beauty', 'Away', "Ed'ard Cuttle", 'Deeper', 'Trump', 'Landlady', 'Peter Piper', 'Rathcal', 'Polly', 'Quadrilles', 'Mr. James Gillespie', 'Healthy', 'Ellie', 'Ned', 'Cocker', 'Haroun Alraschid', 'Joey Bagstock', 'Mrs Perch', 'Mrs MacStinger', 'Stephen Blackpool', 'Young', 'Calomel', 'Orthography', 'Five', 'Sales', 'Hatchet', 'Nick', 'Kingston', 'Enough', 'Ville', 'Thus Florence', 'Beautiful', 'Jeffries', 'Fox', 'Perkins', 'Listen', 'Pankey', 'Miss Gradgrind', 'Philip', 'Mith Thquire', 'Mr. Jarvis Lorry', 'Streaker', 'Heavenly', 'Nay', 'Rain', 'Frenchman', 'Finchley', 'Doctor Parker Peps', 'Edit', 'Ivory', 'Tooley Street', 'Peruvian Miner', 'Fareway', 'MR. BOUNDERBY', 'Josiah Bounderby Esquire', 'Mrs Toots', 'Six', 'Guineas', 'Southcott', 'Someone', 'Barnet', 'Mr. Blackpool', 'Monsieur Lorry', 'Ginger', 'Simon', 'Shadows Mr', 'Neptune', 'Berry Mrs Wickam', 'Houses', 'Beef Shop', 'Coffee House', 'Twinkle', 'Hush', 'Engine Fireman', 'Skettles', 'Walters', 'Everybody', 'Chrisen', 'Baggs', 'Escape', 'Happily', 'Curse', 'Spirit', 'True', 'Haply', 'La Prairie', 'Lady Cankaby', 'Toodle Junior', 'Blue Beard', 'Jim', 'Rome', 'Infidel', 'Slightly', 'Little Hatchet', 'Anyone', 'Sir Barnet', 'Crafty', 'Wickam', 'Dolt', 'Normandy', 'John Bull', 'Cornelia Blimber', 'Whether Mrs MacStinger', 'Left', 'Hamlet', 'Pretty', 'Many', 'Charles', 'Curtius', 'Miss Blimber', 'Moosulmaun', 'Dust', 'Captain Bunsby', 'Home', 'Father', 'Citizen Manette', 'Lottery', 'Elizabeth', 'Lilburn W. Baggs', 'Sole', 'Thquire', 'Hem', 'Death', 'Magog', 'Alfred', 'Plautus', 'Hide Charles', 'Hock', 'Hawkyard', 'Dress', 'Madame', 'Mine', 'Joe', 'Cornelia', 'Cupids', 'Darkest', 'Seraglio', 'Somebody', 'Grief', 'Spies', 'Caius Marius', 'Citizen', 'Philadelphia', 'Art', 'Vengeance', 'Simply', 'Skewton', 'Mum', 'Debauchery', 'Often', 'Mr. Joseph Smith', 'Society', 'Drownded', 'Said Mr. Granville', 'MR. ARPIN', 'English', 'Sissy Jupe', 'Sir Parker Peps', 'Haggard Saint Antoine', 'Little Gunpowder', 'Dumb', 'Awast', 'Mr. Jeremiah Cruncher', 'Fourthy', 'La Force', 'Young Gay', 'Charles Dickens', 'Uncle Sol Captain Cuttle', 'Mr. Arpin', 'Chesapeake Bay', 'Furnished', 'Tetterby', 'Scholar', 'Tony Lumpkin', 'Rage', 'Meaner', 'Dick Jones', 'Silent', 'Mr. Mitchell', 'Law', 'See', 'Floy', 'Brown', 'Table Rock', 'Mr. Bridgman', 'George', 'Blimber', 'Habit', 'Cupid', 'Future', 'Take', "Mr. M'Choakumchild", 'Victim', 'Edward', 'Steamingine', 'Adam Smith', 'Heaven', 'Inquest', 'Jerusalem Buildings', 'Hark', 'Giles', 'Jest Book', 'Polly Toodle', 'Lady Jane Grey', 'Baxter', 'Belinda Bates', 'Ovid', 'Mrs Impudence', 'Caliph Haroun Alraschid', 'Cincinnati', 'Uncle Sol', 'Anthony', 'Aunt', 'Soho', 'Joseph B', 'Jupe', 'Oliver', 'Mr. Sully', 'Sooth', 'Cousin', 'Mildew', 'Knife', 'Partially', 'Anne', 'Public Life', 'Green', 'Certainly', 'Mr. Thomas', 'Grosvenor Square', 'Jollson', 'Wind', 'Chops', 'Magna Charta', 'Cove', 'Widge', 'Enterprise', 'Pray', 'Homeless', 'Quick', 'Love', 'STEPHEN', 'Swollen', 'Barsad', 'Mrs Toodle', 'Mr. Taylor', 'Whereupon Florence', 'Sparsit', 'Doctor', 'Sleepy Hollow', 'Eve', 'Doctors', 'Marquis', 'Thank God', 'Mean', 'Haroun', 'Bishop Butler', 'Gradgrind', 'Roger Cly', 'Dances', 'Lighter', 'Mary Daws', 'Rob', 'Arcade', 'Milly', 'Likewise', 'Jove', 'Pod', 'Judas', 'Angels', 'Levi', 'Edith Dombey', 'Alone', 'Michaelmas', 'Mister Toots', 'Doctor Manette', 'Happy New Year', 'De Lampert', 'Jem', 'Barker', 'Charles Darnay', 'Little', 'Lady', 'Josiah', 'Millennium', 'Brook Street', 'Pilkins', 'Marwood', 'Thus Miss Pross', 'Dishonest Faction', 'Anywheres', 'Sir Gaston Fareway', 'Solemn', 'Little Paul Dombey', 'Master Briggs', 'Gills', 'Careless', 'Ratcliffe', 'Railroad', 'Pardon', 'Forward', 'Arms', 'Manette', 'Turk', 'Timely Provision', 'Adams', 'Scanty', 'Oho', 'Twelfth Night', 'Mr. Bounderby', 'Granger', 'Castle', 'Hail Columbia', 'Dear Di', 'Angry', 'Divine Sermon', 'Gentleman', 'Swiftly', 'Loo Bounderby', 'Citizen Defarge', 'Married Females', 'Good', 'Juliana MacStinger', 'Holly', 'Shadowy', 'Husband', 'Giles Scroggins', 'Moloch', 'Walk', 'Fire', 'Frederick', 'Gog', 'Poor Walter', 'Hall', 'Trottle', 'Blackpool', 'Seven', 'Belinda', 'Omega', 'Bush', 'Charleston'}

9.2. Most popular name:  
    ('Dombey', 1780)

