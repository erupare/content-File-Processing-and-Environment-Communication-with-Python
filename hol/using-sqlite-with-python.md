# Using SQLite with Python

## Basic Lab Information

- Primary Topic: DevOps

- Categories: AWS, DevOps

- Difficulty: Beginner

- Time Limit: 45 minutes

- Avg Completion Time: 30 minutes

- Tags: 
    `Python` 
    `SQLite` 
    `CRUD` 
    `Databases` 
    `File Processing and Environment Communication with Python`

## Lab Description:
In this lab, you will learn to perform CRUD processes on a SQLite database.  You will first create a datatable and then add data to it.  You will practice reading data from the table and need to make corrections to the data.

The skills you practice and learn in this lab will be applicable to most other major databases.  You will be able to reuse your code here by just replacing the database engine connection with the one you are using. 

You will need basic python programming and SQL skills for this lab:
- [Certified Associate in Python Programming Certification](https://linuxacademy.com/cp/modules/view/id/470)
- [SQL Deep Dive](https://linuxacademy.com/cp/modules/view/id/407)


## Lab Instructions:

Atlantic Publishing is a startup publishing house with the motto "We print what others won't!".  They started keeping written lists that summarized the author contracts.  Finally deciding they need to have a more robust method they wanted to move to a database.  The first step they took was to create a python list of their written summarized data.  But were unsure how to proceed past that point.  So they have hired you to create and maintain their database, as well as, provide them needed data on the spot.  They have left the choice of the database up to you.


## Lab Objectives

### Objective 1: Create a datatable in SQLite.

One of the things we will have to do over and over is connect to the database.  So first, we will write a function that we can then import into each of our separate tasks. The file we will use is `connect_db.py`. The function should be called `get_db_connection` and should return a connection and cursor object when called.


```python
# connect_db.py

import sqlite3

def get_db_connection():
    
    # Make connection to db called cxn
    cxn = sqlite3.connect(DB_NAME)

    # Create a cursor to db named cur
    cur = cxn.cursor()
    
    # return them both
    return cxn, cur


```

Now we need to create the table and populate it.  File `create_table.py` has a skeleton for this work.  There are two tests in this file; these tests check that the database table exists and that the table has 6 rows of data. 

The file contains the data and sql statements needed, you supply the code to process the sql statement with Python and SQLite. To begin with run `python create_table.py`.  The `main` function is provided for you.  This should return an `assert` error with the statement `table does not exist.`

Let's create the table. 


```python
# create_table.py

def create_table():
    """
    Creates a table ready to accept our data.
    """
    
    create_table = """ CREATE TABLE authors(
        ID          INTEGER PRIMARY KEY     AUTOINCREMENT,
        author      TEXT                NOT NULL,
        title       TEXT                NOT NULL,
        pages       INTEGER             NOT NULL,
        due_date    CHAR(15)            NOT NULL
    )   
    """
    
    # get db connections
    cxn, cur = get_db_connection()
        
    # Send sql query to cur and then execute it
    cur.execute(create_table)
    cxn.commit()
        
    # close database connections
    cur.close()
    cxn.close()

```

Now that we have written the code, let's check our test; run `python create_table.py`.  You should not see the error `table does not exist.` but instead should see `The table does not have six rows.`. This means that the table was created and only needs to be populated.


Now let's populate the table we just created with the data provided.  

**HINT: You can provide the sql statement and pass a list of data to cur.execute.  For example, cur.execute(sql, data).***


```python
def populate_table():
    
    # notice the ? at the end of the statement, this tells it get the values from the data passed in
    sql_stmt = ''' INSERT INTO authors(author,title,pages,due_date) VALUES(?,?,?,?); '''
    
    # get db connections
    cxn, cur = get_db_connection()
        
    # Send sql query to request
    # remove header row from contract_list
    del contract_list[0]

    # Use execute many to load data
    cur.executemany(sql_stmt, contract_list  )
    cxn.commit()

    # close database connection.
    cur.close()
    cxn.close()
```

Test the code with `python create_table.py`.  All tests should pass.

**Congratulations!**  You have created the table and populated it.  You are now ready to process requests by the Atlantic Publishing staff.

### Objective 2: Read From Datatable
The Contracts department has asked for a list of all upcoming books, showing the author, the title, and the due date.

The file `read_data.py` has the skeleton file for you.  Again, run `python read_data.py` and you should see an error with the message `the results do not match the expected`.

Let's complete the function `read_data_from_db`.  Make the function return the results from the `sql_query` so the testing function can be ran.  There is also some code in the `main` function that prints the data so you can review.


```python
def read_data_from_db():
    """
    Return data from database.
    """
    
    sql_query = ''' SELECT author,title,due_date FROM authors; '''
    
    # get db connections
    cxn, cur = get_db_connection()
        
    # send sql query to request
    cur.execute(sql_query)
    results = cur.fetchall()

    #closing database connection.
    cur.close()
    cxn.close()  

    return results
```

Again, run `python read_data.py` and you should not see an error but should see the data that will be passed to the Contracts department.

**Congratulations!** The Contracts department was thorougly impressed with your ability to deliver the data.

### Objective 3: Update and Delete Rows
The  Contracts department sends back the data with the follwoing notes:
- "Smith, Jackson" is duplicated and neither is correct, the due date is "2020-10-31" and pages are 600.

The file `update_data.py` has the skeleton file for you.  Again, run `python update_data.py` and you should see an error with the message `the number of Smith Jackson rows is incorrect`.

Let's complete the function `delete_data_from_db`.  Write a script to delete one of the "Smith, Jackson".

```python
def delete_data_from_db():
    """
    Delete selected data from database.
    """
    
    sql_query = ''' DELETE FROM authors WHERE (author="Smith, Jackson" AND pages=400); '''
    
    # get db connections
    cxn, cur = get_db_connection()

    # Send sql query to request
    cur.execute(sql_query)
    cxn.commit()

    # close database connection.
    cur.close()
    cxn.close()    

```

Now that we have written the code, let's check our test; run `python update_data.py`.  You should not see the error `the number of Smith Jackson rows is incorrect` but instead should see `due date not updated correctly`. This means that you have deleted a duplicate row and now just need to fix the typo in the due date column for the remaining entry.

Now let's fix the due date typo.  


```python
def update_data():
    sql_query = ''' UPDATE authors SET due_date="2020-10-31" WHERE author="Smith, Jackson"; '''
    
    # get db connections
    cxn, cur = get_db_connection()

    # Send sql query to request
    cur.execute(sql_query)
    cxn.commit()

    #closing database connection.
    cur.close()
    cxn.close() 
```

Again, run `python update_data.py` and you should not see an error so you know the data was updated correctly.
**Congratulations!** You have shown that you can update data in the data table.


### Objective 4: Update table
The pubishing house has decided to add a Genre column to the datatable.  They have a list of titles and genres.
``` python
[
    ["title", "genre"],
    ["Oh Python! My Python!", "biography"],
    ["Fun with Django", "satire"],
    ["When Bees Attack! The Horror!", "horror"],
    ["Martin Buber's Philosophies", "guide"],
    ["The Sun Also Orbits", "mystery"]
]
```
The file `update_table.py` has the skeleton file for you.  Again, run `python update_table.py` and you should see an error with the message `column was not added properly`.

Let's complete the function `add_column_to_db`.  



```python
def add_column_to_db():
    """
    Add a column to the table.
    """
    
    sql_query = ''' ALTER TABLE authors ADD COLUMN genre CHAR(15); '''
    
    # get db connections
    cxn, cur = get_db_connection()

    # Send sql query to request
    cur.execute(sql_query)
    cxn.commit()

    # close database connection.
    cur.close()
    cxn.close() 
```

Now that we have written the code, let's check our test; run `python update_table.py`.  You should not see the error `column was not added properly` but instead should see `genre did not populate correctly`. 

So let's populate the `genre` column.


```python
def add_data_to_column():
    
    sql_query = ''' f"UPDATE authors SET genre = \"{row[1]}\" WHERE title = \"{row[0]}\";" '''

    genre_data = [
        ["title", "genre"],
        ["Oh Python! My Python!", "biography"],
        ["Fun with Django", "satire"],
        ["When Bees Attack! The Horror!", "horror"],
        ["Martin Buber's Philosophies", "guide"],
        ["The Sun Also Orbits", "mystery"]
    ]
    
    # get db connections
    cxn, cur = get_db_connection()

    # Send sql query to request
    # remove header row from genre_data
    del genre_data[0]

    # Use execute many to load data
    cur.executemany(sql_stmt, genre_data)
    cxn.commit()


    # close database connection.
    cur.close()
    cxn.close()
```

Let's check our test; run `python update_table.py`.  You should not see anything failing.

**Congratulations!**. You have proven yourself to be valuable member of Atlantic Publishing.

# LaaS Settings
``` json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "Cloudformation template with 1 instance",
  "Mappings": {
    "SubnetConfig": {
      "VPC": {
        "CIDR": "10.0.0.0/16"
      },
      "Public1": {
        "CIDR": "10.0.1.0/24"
      }
    }
  },
  "Resources": {
    "VPC": {
      "Type": "AWS::EC2::VPC",
      "Properties": {
        "EnableDnsSupport": "true",
        "EnableDnsHostnames": "true",
        "CidrBlock": {
          "Fn::FindInMap": [
            "SubnetConfig",
            "VPC",
            "CIDR"
          ]
        },
        "Tags": [
          {
            "Key": "Name",
            "Value": "LinuxAcademy"
          },
          {
            "Key": "Application",
            "Value": {
              "Ref": "AWS::StackName"
            }
          },
          {
            "Key": "Network",
            "Value": "VPC"
          }
        ]
      }
    },
    "PublicSubnet1": {
      "Type": "AWS::EC2::Subnet",
      "Properties": {
        "VpcId": {
          "Ref": "VPC"
        },
        "AvailabilityZone": {
          "Fn::Select": [
            "0",
            {
              "Fn::GetAZs": ""
            }
          ]
        },
        "CidrBlock": {
          "Fn::FindInMap": [
            "SubnetConfig",
            "Public1",
            "CIDR"
          ]
        },
        "Tags": [
          {
            "Key": "Application",
            "Value": {
              "Ref": "AWS::StackName"
            }
          },
          {
            "Key": "Network",
            "Value": "Public1"
          }
        ]
      }
    },
    "InternetGateway": {
      "Type": "AWS::EC2::InternetGateway",
      "Properties": {
        "Tags": [
          {
            "Key": "Application",
            "Value": {
              "Ref": "AWS::StackName"
            }
          },
          {
            "Key": "Network",
            "Value": "Public"
          }
        ]
      }
    },
    "GatewayToInternet": {
      "Type": "AWS::EC2::VPCGatewayAttachment",
      "Properties": {
        "VpcId": {
          "Ref": "VPC"
        },
        "InternetGatewayId": {
          "Ref": "InternetGateway"
        }
      }
    },
    "PublicRouteTable": {
      "Type": "AWS::EC2::RouteTable",
      "Properties": {
        "VpcId": {
          "Ref": "VPC"
        },
        "Tags": [
          {
            "Key": "Application",
            "Value": {
              "Ref": "AWS::StackName"
            }
          },
          {
            "Key": "Network",
            "Value": "Public"
          }
        ]
      }
    },
    "PublicRoute": {
      "Type": "AWS::EC2::Route",
      "DependsOn": "GatewayToInternet",
      "Properties": {
        "RouteTableId": {
          "Ref": "PublicRouteTable"
        },
        "DestinationCidrBlock": "0.0.0.0/0",
        "GatewayId": {
          "Ref": "InternetGateway"
        }
      }
    },
    "PublicSubnetRouteTableAssociation1": {
      "Type": "AWS::EC2::SubnetRouteTableAssociation",
      "Properties": {
        "SubnetId": {
          "Ref": "PublicSubnet1"
        },
        "RouteTableId": {
          "Ref": "PublicRouteTable"
        }
      }
    },
    "PublicNetworkAcl": {
      "Type": "AWS::EC2::NetworkAcl",
      "Properties": {
        "VpcId": {
          "Ref": "VPC"
        },
        "Tags": [
          {
            "Key": "Application",
            "Value": {
              "Ref": "AWS::StackName"
            }
          },
          {
            "Key": "Network",
            "Value": "Public"
          }
        ]
      }
    },
    "InboundHTTPPublicNetworkAclEntry": {
      "Type": "AWS::EC2::NetworkAclEntry",
      "Properties": {
        "NetworkAclId": {
          "Ref": "PublicNetworkAcl"
        },
        "RuleNumber": "100",
        "Protocol": "6",
        "RuleAction": "allow",
        "Egress": "false",
        "CidrBlock": "0.0.0.0/0",
        "PortRange": {
          "From": "80",
          "To": "80"
        }
      }
    },
    "InboundHTTPSPublicNetworkAclEntry": {
      "Type": "AWS::EC2::NetworkAclEntry",
      "Properties": {
        "NetworkAclId": {
          "Ref": "PublicNetworkAcl"
        },
        "RuleNumber": "101",
        "Protocol": "6",
        "RuleAction": "allow",
        "Egress": "false",
        "CidrBlock": "0.0.0.0/0",
        "PortRange": {
          "From": "443",
          "To": "443"
        }
      }
    },
    "InboundSSHPublicNetworkAclEntry": {
      "Type": "AWS::EC2::NetworkAclEntry",
      "Properties": {
        "NetworkAclId": {
          "Ref": "PublicNetworkAcl"
        },
        "RuleNumber": "102",
        "Protocol": "6",
        "RuleAction": "allow",
        "Egress": "false",
        "CidrBlock": "0.0.0.0/0",
        "PortRange": {
          "From": "22",
          "To": "22"
        }
      }
    },
    "InboundEmphemeralPublicNetworkAclEntry": {
      "Type": "AWS::EC2::NetworkAclEntry",
      "Properties": {
        "NetworkAclId": {
          "Ref": "PublicNetworkAcl"
        },
        "RuleNumber": "103",
        "Protocol": "6",
        "RuleAction": "allow",
        "Egress": "false",
        "CidrBlock": "0.0.0.0/0",
        "PortRange": {
          "From": "1024",
          "To": "65535"
        }
      }
    },
    "OutboundPublicNetworkAclEntry": {
      "Type": "AWS::EC2::NetworkAclEntry",
      "Properties": {
        "NetworkAclId": {
          "Ref": "PublicNetworkAcl"
        },
        "RuleNumber": "100",
        "Protocol": "6",
        "RuleAction": "allow",
        "Egress": "true",
        "CidrBlock": "0.0.0.0/0",
        "PortRange": {
          "From": "0",
          "To": "65535"
        }
      }
    },
    "PublicSubnetNetworkAclAssociation1": {
      "Type": "AWS::EC2::SubnetNetworkAclAssociation",
      "Properties": {
        "SubnetId": {
          "Ref": "PublicSubnet1"
        },
        "NetworkAclId": {
          "Ref": "PublicNetworkAcl"
        }
      }
    },
    "EC2SecurityGroup": {
      "Type": "AWS::EC2::SecurityGroup",
      "Properties": {
        "GroupDescription": "Enable access to the EC2 host",
        "VpcId": {
          "Ref": "VPC"
        },
        "SecurityGroupIngress": [
          {
            "IpProtocol": "-1",
            "FromPort": "-1",
            "ToPort": "-1",
            "CidrIp": "0.0.0.0/0"
          }
        ]
      }
    },
    "SGBaseIngress": {
      "Type": "AWS::EC2::SecurityGroupIngress",
      "Properties": {
        "GroupId": {
          "Ref": "EC2SecurityGroup"
        },
        "IpProtocol": "tcp",
        "FromPort": "80",
        "ToPort": "80",
        "SourceSecurityGroupId": {
          "Ref": "EC2SecurityGroup"
        }
      }
    },
    "Workstation": {
      "Type": "AWS::EC2::Instance",
      "CreationPolicy": {
        "ResourceSignal": {
          "Count": 1
        }
      },
      "Properties": {
        "InstanceType": "t3.medium",
        "UserData": {
          "Fn::Base64": {
            "Fn::Join": [
              "",
              [
                "#!/bin/bash -xe\n",
                "/bin/echo '%password%' | /bin/passwd cloud_user --stdin\n",
                "/usr/sbin/setenforce 0\n",
                "/usr/bin/systemctl stop firewalld\n",
                "export PYTHONPATH=\"${PYTHONPATH}:/usr/local/lib/python2.7/site-packages/\"\n",
                "cd /home/cloud_user/\n",
                "echo 'eval \"$(pyenv init -)\"' >> /home/cloud_user/.bashrc\n",
                "echo 'pyenv shell 3.8.2' >> /home/cloud_user/.bashrc\n",
                "git init\n",
                "git remote add origin https://github.com/linuxacademy/content-File-Processing-and-Environment-Communication-with-Python.git\n",
                "git config core.sparsecheckout true\n",
                "echo 'hol/*' >> .git/info/sparse-checkout\n",
                "git pull --depth=2 origin hol-3-sqlite\n",
                "chown -R cloud_user:cloud_user /home/cloud_user/*\n",
                "/opt/aws/bin/cfn-signal -e $? ",
                "         --stack ",
                {
                  "Ref": "AWS::StackName"
                },
                "         --resource Workstation ",
                "         --region ",
                {
                  "Ref": "AWS::Region"
                },
                "\n"
              ]
            ]
          }
        },
        "ImageId": "%ami-204%",
        "NetworkInterfaces": [
          {
            "GroupSet": [
              {
                "Ref": "EC2SecurityGroup"
              }
            ],
            "AssociatePublicIpAddress": "true",
            "DeviceIndex": "0",
            "DeleteOnTermination": "true",
            "SubnetId": {
              "Ref": "PublicSubnet1"
            }
          }
        ]
      }
    }
  },
  "Outputs": {
    "pubIpAddress1": {
      "Description": "Public IP address of Workstation",
      "Value": {
        "Fn::GetAtt": [
          "Workstation",
          "PublicIp"
        ]
      }
    },
    "privIpAddress1": {
      "Description": "Private IP address of Workstation",
      "Value": {
        "Fn::GetAtt": [
          "Workstation",
          "PrivateIp"
        ]
      }
    }
  }
}

```


# Videos & Guide
- Title: Create a datatable in SQLite.
- Description: 
- Video

------
- Title: Read From Datatable.
- Description: 
- Video

-------
- Title: Update and Delete Rows.
- Description: 
- Video

------

- Title: Update table.
- Description: 
- Video

-------
-Diagram



```python

```
