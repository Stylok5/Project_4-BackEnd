python manage.py dumpdata jwt_auth --output jwt_auth/seeds.json --indent=2;
python manage.py dumpdata groups --output groups/seeds.json --indent=2;
python manage.py dumpdata genres --output genres/seeds.json --indent=2;
python manage.py dumpdata games --output games/seeds.json --indent=2;
python manage.py dumpdata ratings --output ratings/seeds.json --indent=2;
python manage.py dumpdata members --output members/seeds.json --indent=2;
python manage.py dumpdata groupchat --output groupchat/seeds.json --indent=2;
