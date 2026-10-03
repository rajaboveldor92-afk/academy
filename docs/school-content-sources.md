# Added school courses and Technology directions

These are original supplemental activities, not a reproduction of an official
Uzbek textbook or a claim of complete state-curriculum alignment. The 22 missing
files now contain four authored units, four unit tests and one final review each.
Reading passages are original; grade 2 uses concrete events, grade 7 adds cause
and evidence, grade 8 adds source limits and competing arguments.

Technology keeps original IDs and saved progress. Shared safety/material lessons
remain visible. Profile recommendations select service/crafts for girls and
technical design for boys; parents can override either recommendation or choose
both. A profile with no gender selection defaults to both. Track tests reference
only that track and shared lessons. The circuit activity is a virtual ideal model.

Primary reference checks for stable facts and grammar (checked 2026-10-03):

- IUPAC, element names and periodic table: https://iupac.org/what-we-do/periodic-table-of-elements/
- USGS, water cycle: https://water.usgs.gov/vizlab/water-cycle/
- USGS, geological learning resources: https://www.usgs.gov/educational-resources/geology-education
- NASA/JPL, force, mass and acceleration: https://www.jpl.nasa.gov/edu/resources/teachable-moment/may-the-force-mass-x-acceleration/
- NASA, electric circuits: https://pwg.gsfc.nasa.gov/Education/welectrc.html
- OpenStax, blood-vessel directions: https://openstax.org/books/anatomy-and-physiology-2e/pages/20-1-structure-and-function-of-blood-vessels
- OpenStax, gas exchange in alveoli: https://openstax.org/books/biology-2e/pages/39-1-systems-of-gas-exchange
- British Council, present perfect: https://learnenglish.britishcouncil.org/free-resources/grammar/b1-b2/present-perfect
- British Council, conditionals: https://learnenglish.britishcouncil.org/free-resources/grammar/b1-b2/conditionals-zero-first-second
- British Council, passive forms: https://learnenglish.britishcouncil.org/free-resources/grammar/b1-b2/passives

Authoring: `tool/content/school/missing_courses.py` and
`tool/content/school/technology.py` (which imports `technology_service.py`).
Both generation paths were run twice and produce identical files.
CI checks bank answers/references, builds every new lesson/test at all three
levels, tests direction filtering, migration and small-phone reading, then
compares every packaged school JSON byte-for-byte with the source.
