function validateUserInput() 
{
    
    var teams = [ "Alabama", "Texas A&M-CC", "Maryland", "West Virginia", "San Diego St.", "Col of Charleston", "Virginia", "Furman", "Creighton", "NC State", "Baylor", "UCSB", "Missouri", "Utah St.", "Arizona", "Princeton",
    "Purdue", "FDU", "Memphis", "FAU", "Duke", "Oral Roberts", "Tenesee", "Louisiana", "Kentucky", "Providence", "Kansas St.", "Montana St.", "Michigan St.", "USC", "Marquette", "Vermont",
    "Houston", "N Kentucky", "Iowa", "Auburn", "Miami (FL)", "Drake", "Indiana", "Kent St.", "Iowa St.", "Pitt", "Xavier", "Kennesaw St.", "Texas A&M", "Penn St.", "Texas", "Colgate",
    "Kansas", "Howard", "Arkansas", "Illinois", "Saint Mary's", "VCU", "UConn", "Iona", "TCU", "Arizona St.", "Gonzaga", "Grand Canyon", "Northwestern", "Boise St.", "UCLA", "UNC Asheville"
    ];

    var winner = document.getElementById("winner").value;
    console.log(winner);

    if(teams.indexOf(winner) == -1 && winner !== "")
    {
        alert("Specified winner must be one of the 64 teams.");
        document.userInput.winner.focus();
        return false;
    }

    i = 0;
    while(i < 5)
    {
        var temp = document.getElementById("preferences" + i);
        if(temp !== null)
        {
            if(teams.indexOf(temp.value) == -1 && temp.value !== "")
            {
                alert("Preference input must be one of the 64 teams.");
                return false;
            }
        }
        i++;
    }

    return true;
}

var idNo = 1;

function createNewInputFields() 
{
    if(idNo < 5) 
    {
        var container = document.getElementById('prefinput');
        const newElem = document.createElement("input");
        newElem.setAttribute("list", "teams");
        newElem.setAttribute("class", "form-control mt-1");
        newElem.setAttribute("id", "preferences" + idNo);
        newElem.setAttribute("name", "preferences" + idNo);
        container.appendChild(newElem);
        // heightChange = 75 + (idNo * 5);
        // document.getElementById("border-box").style.height = String(heightChange) + "%";
        idNo++;
    }
    else
    {
        alert("Maximum 5 teams can be given preference.");
        document.userInput.winner.focus();
    }
}