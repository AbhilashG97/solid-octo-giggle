# Mock AHMS API :school:

This is very **minimilistic mock ahms API**. It is live and can be found at [here](https://mock-ahms.herokuapp.com/)

## Documentation

**GET all results**

https://mock-ahms.herokuapp.com/v1/resources/ahms/all

**GET result based on Student ID**

https://mock-ahms.herokuapp.com/v1/resources/ahms?student_id=18001

:warning: Add required Student ID value after ```?student_id=``` 

:boom: The API currently **only** provides data for 8 students, i.e - 18001 to 18008

**GET result based on stay back**

https://mock-ahms.herokuapp.com/v1/resources/ahms?has_stayback=1

:warning: Add required ```has_stayback``` value after ```?has_stayback=```

:boom: ```has_stayback``` only takes **boolean values**, i.e **either 1 or 0** 
