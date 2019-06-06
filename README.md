# Mock Amrita Hostel Management System(AHMS) API :school:

This is very **minimilistic mock ahms API**. It is live and can be found at [here](https://mock-ahms.herokuapp.com/). 

:warning: This API has been created for **teaching purposes** only. 

## API Documentation

**GET all results**

https://mock-ahms.herokuapp.com/v1/resources/ahms/all

**GET result based on Student ID**

https://mock-ahms.herokuapp.com/v1/resources/ahms?student_id=18001

:warning: Add required Student ID value after ```?student_id=``` 

:boom: The API currently **only** provides data for 8 students, i.e 18001 to 18008

**GET result based on stay back**

https://mock-ahms.herokuapp.com/v1/resources/ahms?has_stayback=1

:warning: Add required ```has_stayback``` value after ```?has_stayback=```

:boom: ```has_stayback``` only takes **boolean values**, i.e **either 1 or 0** 

## Some useful Git Commands

1.  Viewing the status of your repostory
    
    ```git
    git status
    ```
    This command will show the current status of your repository
    
1.  Adding (Staging) files to git

    ```git
    git add -A
    ```
    
    :warning: This command will add all ```modified and untracted files```.
    
1.  Commiting a file
    
    ```git 
    git commit -m "YOUR COMMIT MESSAGE"
    ```
    :warning: Replace ```YOUR COMMIT MESSAGE``` with a suitable commit message.
    
1.  Uploading/pushing your files to a remote repository

    ```git
    git push origin master
    ```
    
    :warning: The above command will push/upload all your files to the ```master``` branch of your repository.
   
:star: To know more on Git, please have a look [here](https://git-scm.com/book/en/v2).
