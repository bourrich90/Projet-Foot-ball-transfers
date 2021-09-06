from pydantic import BaseModel

# table Football_transfert columns
class Football_transfert(BaseModel):
    Name : str
    Position: str
    Age :int
    Team_from :str
    League_from : str
    Team_to :str
    League_to :str
    Season :str
    Market_value : float 
    Transfer_fee : float