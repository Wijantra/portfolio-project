## Portfolio
Portfolio Website with Django Framework from Principle of Software Architecture subject
##### By wijantra Cojamnong 6110545627


## How to run

Step1: Clone this repository and change your current working directory 
```bash
    git clone https://github.com/Wijantra/portfolio-project
    cd portfolio-project
```

Step2: Install virtual enviroment
```bash
    pip install virtualenv
```

Step3: Create new virtual enviroment
```bash
    virtualenv env
```

Step4: Install all required packages
```bash
    pip install -r requirements.txt
```

Step5: Create database tables
```bash
    python manage.py migrate
```

Step6: Run server 
```bash
    python manage.py runserver
```