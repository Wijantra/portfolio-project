## Portfolio
Portfolio Website with Django Framework from Principle of Software Architecture subject
##### By wijantra Cojamnong 6110545627


## How to run


Step1: Install virtual enviroment
```bash
    pip install virtualenv
```

Step2: Clone this repository and change your current working directory 
```bash
    git clone https://github.com/Wijantra/portfolio-project
    cd portfolio-project
```

Step3: Create new virtual enviroment
```bash
    virtualenv env
```

Step4: Activate virtualenv
```bash
    \path\to\env\Scripts\activate
```

Step5: After activate virtualenv, install all required packages
```bash
    pip install -r requirements.txt
```

Step6: Create database tables
```bash
    python manage.py migrate
```

Step7: Collect static
```bash
    python manage.py collectstatic
```

Step8: Run server 
```bash
    python manage.py runserver
```