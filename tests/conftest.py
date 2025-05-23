import pytest
from pydantic_settings import BaseSettings

db_structure = {
    "Rating": {
        "Date": {
            "Type": ["date"],
            "Params": {
                "PrimaryKey": ["Y", "A"],
                "FKey": [],
                "Index": [1, 1, "A", "U"],
                "NN": "Y",
                "B": "",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Rate of publication",
        },
        "Name": {
            "Type": ["varchar", 30],
            "Params": {
                "PrimaryKey": ["Y", "A"],
                "FKey": [1, 2, "Member", "Name", "C", "C"],
                "Index": [],
                "NN": "Y",
                "B": "",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Name from Member",
        },
        "Surname": {
            "Type": ["varchar", 45],
            "Params": {
                "PrimaryKey": ["Y", "A"],
                "FKey": [1, 1, "Member", "Surname", "C", "C"],
                "Index": [],
                "NN": "Y",
                "B": "",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Surname from Member",
        },
        "Rating": {
            "Type": ["int"],
            "Params": {
                "PrimaryKey": ["", ""],
                "FKey": [],
                "Index": [],
                "NN": "",
                "B": "",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Rating of member",
        },
        "OrgMemberId": {
            "Type": ["int"],
            "Params": {
                "PrimaryKey": ["", ""],
                "FKey": [],
                "Index": [1, 2, "A", "U"],
                "NN": "",
                "B": "",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Rating of member",
        },
    },
    "Member": {
        "Surname": {
            "Type": ["varchar", 45],
            "Params": {
                "PrimaryKey": ["Y", "A"],
                "FKey": [],
                "Index": [],
                "NN": "Y",
                "B": "",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Surname of member",
        },
        "Name": {
            "Type": ["varchar", 30],
            "Params": {
                "PrimaryKey": ["Y", "A"],
                "FKey": [],
                "Index": [],
                "NN": "Y",
                "B": "",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Name of the member",
        },
        "SosSec": {
            "Type": ["varchar", 10],
            "Params": {
                "PrimaryKey": ["", ""],
                "FKey": [],
                "Index": [1, 1, "D", "U"],
                "NN": "Y",
                "B": "",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Sosial security nr filled with zeros",
        },
        "Country": {
            "Type": ["char", 3],
            "Params": {
                "PrimaryKey": ["", ""],
                "FKey": [1, 1, "Country", "Code", "R", "C"],
                "Index": [2, 2, "A", "U"],
                "NN": "Y",
                "B": "",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Country passport",
        },
        "PassportNr": {
            "Type": ["char", 15],
            "Params": {
                "PrimaryKey": ["", ""],
                "FKey": [],
                "Index": [2, 1, "D", "U"],
                "NN": "Y",
                "B": "",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Passport number",
        },
        "Race": {
            "Type": ["tinyint"],
            "Params": {
                "PrimaryKey": ["", ""],
                "FKey": [],
                "Index": [],
                "NN": "Y",
                "B": "",
                "UN": "Y",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "1",
            },
            "Possible Values": "1=White,2=Black",
            "Comment": "Race of member",
        },
        "RegDateTime": {
            "Type": ["datetime"],
            "Params": {
                "PrimaryKey": ["", ""],
                "FKey": [],
                "Index": [3, 1, "D", "U"],
                "NN": "",
                "B": "",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Registration date",
        },
        "Picture": {
            "Type": ["blob"],
            "Params": {
                "PrimaryKey": ["", ""],
                "FKey": [],
                "Index": [],
                "NN": "",
                "B": "Y",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Photo of member",
        },
        "ActiveStatus": {
            "Type": ["boolean"],
            "Params": {
                "PrimaryKey": ["", ""],
                "FKey": [],
                "Index": [],
                "NN": "",
                "B": "",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Active | Inactive",
        },
        "BirthYear": {
            "Type": ["int"],
            "Params": {
                "PrimaryKey": ["", ""],
                "FKey": [],
                "Index": [],
                "NN": "",
                "B": "",
                "UN": "Y",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Birth year of member",
        },
        "DOB": {
            "Type": ["date"],
            "Params": {
                "PrimaryKey": ["", ""],
                "FKey": [],
                "Index": [],
                "NN": "",
                "B": "",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Date of Birth",
        },
    },
    "Country": {
        "Code": {
            "Type": ["char", 3],
            "Params": {
                "PrimaryKey": ["Y", "D"],
                "FKey": [],
                "Index": [],
                "NN": "Y",
                "B": "",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "3 digit country code",
        },
        "Description": {
            "Type": ["varchar", 30],
            "Params": {
                "PrimaryKey": ["", ""],
                "FKey": [],
                "Index": [],
                "NN": "",
                "B": "",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Name of country",
        },
    },
    "Organization": {
        "OrgId": {
            "Type": ["bigint"],
            "Params": {
                "PrimaryKey": ["Y", "D"],
                "FKey": [],
                "Index": [1, 1, "A", "U"],
                "NN": "Y",
                "B": "",
                "UN": "Y",
                "ZF": "",
                "AI": "Y",
                "G": "Y",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Organization id auto generated",
        },
        "OrgName": {
            "Type": ["varchar", 20],
            "Params": {
                "PrimaryKey": ["", ""],
                "FKey": [],
                "Index": [2, 1, "A", ""],
                "NN": "Y",
                "B": "",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Organization name",
        },
        "RegFee": {
            "Type": ["decimal", 5, 2],
            "Params": {
                "PrimaryKey": ["", ""],
                "FKey": [],
                "Index": [],
                "NN": "",
                "B": "",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Registration fee",
        },
        "OpenTrading": {
            "Type": ["time"],
            "Params": {
                "PrimaryKey": ["", ""],
                "FKey": [],
                "Index": [],
                "NN": "",
                "B": "",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Opening time for trading",
        },
    },
    "MemberOrg": {
        "Surname": {
            "Type": ["varchar", 45],
            "Params": {
                "PrimaryKey": ["Y", "A"],
                "FKey": [],
                "Index": [],
                "NN": "Y",
                "B": "",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Surname from Member",
        },
        "Name": {
            "Type": ["varchar", 30],
            "Params": {
                "PrimaryKey": ["Y", "A"],
                "FKey": [],
                "Index": [],
                "NN": "Y",
                "B": "",
                "UN": "",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "Name from Member",
        },
        "OrgId": {
            "Type": [
                "bigint",
            ],
            "Params": {
                "PrimaryKey": ["Y", "D"],
                "FKey": [],
                "Index": [],
                "NN": "Y",
                "B": "",
                "UN": "Y",
                "ZF": "",
                "AI": "",
                "G": "",
                "DEF": "",
            },
            "Possible Values": "",
            "Comment": "OrgId from Organizarion",
        },
    },
}


class Settings(BaseSettings):
    INSTALLER_USERID: str = ""
    INSTALLER_PWD: str = ""
    MYSQL_HOST: str = ""
    MYSQL_TCP_PORT: int = "3306"
    MYSQL_DATABASE: str = ""
    MYSQL_PWD: str = ""
    MYSQL_ROOT_PASSWORD: str = ""
    VENV_ENVIRONMENT: str = "prod"


@pytest.fixture
def get_settings() -> Settings:
    return Settings()
    # pass
