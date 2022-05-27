
let human_score = 0;
let computer_score = 0;

function game(human_choice)
{   
    let computer_choice = ["rock", "paper", "scissors"][Math.floor(Math.random() * 3)];

    if (human_choice === "rock" && computer_choice === "paper")
    {
        computer_score = computer_score + 1;
        document.getElementById("computer_score").innerHTML = computer_score;
        document.getElementById('human_choice_image').src = "/static/"+human_choice+".gif";
        document.getElementById('computer_choice_image').src = "/static/"+computer_choice+".gif";
    }

    else if (human_choice === "rock" && computer_choice === "scissors")
    {
        human_score = human_score + 1;
        document.getElementById("human_score").innerHTML = human_score;
        document.getElementById('human_choice_image').src = "/static/"+human_choice+".gif";
        document.getElementById('computer_choice_image').src = "/static/"+computer_choice+".gif";
    }
    else if (human_choice === "paper" && computer_choice === "rock")
    {
        human_score = human_score + 1;
        document.getElementById("human_score").innerHTML = human_score;
        document.getElementById('human_choice_image').src = "/static/"+human_choice+".gif";
        document.getElementById('computer_choice_image').src = "/static/"+computer_choice+".gif";
    }

    else if (human_choice === "paper" && computer_choice === "scissors")
    {
        computer_score = computer_score + 1;
        document.getElementById("computer_score").innerHTML = computer_score;
        document.getElementById('human_choice_image').src = "/static/"+human_choice+".gif";
        document.getElementById('computer_choice_image').src = "/static/"+computer_choice+".gif";
    }

    else if (human_choice === "scissors" && computer_choice === "paper")
    {
        human_score = human_score + 1;
        document.getElementById("human_score").innerHTML = human_score;
        document.getElementById('human_choice_image').src = "/static/"+human_choice+".gif";
        document.getElementById('computer_choice_image').src = "/static/"+computer_choice+".gif";
    }

    else if (human_choice === "scissors" && computer_choice === "rock")
    {
        computer_score = computer_score + 1;
        document.getElementById("computer_score").innerHTML = computer_score;
        document.getElementById('human_choice_image').src = "/static/"+human_choice+".gif";
        document.getElementById('computer_choice_image').src = "/static/"+computer_choice+".gif";
    }

    else if (human_choice === computer_choice)
    {
        document.getElementById("human_score").innerHTML = human_score;
        document.getElementById("computer_score").innerHTML = computer_score;
        document.getElementById('human_choice_image').src = "/static/"+human_choice+".gif";
        document.getElementById('computer_choice_image').src = "/static/"+computer_choice+".gif";
    }
}

function play_again()
{   
    human_score = 0;
    computer_score = 0;
    
    document.getElementById("computer_score").innerHTML = computer_score;
    document.getElementById("human_score").innerHTML = human_score;

    document.getElementById('human_choice_image').src = "/static/zero.gif";
    document.getElementById('computer_choice_image').src = "/static/zero.gif";
}