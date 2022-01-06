const squareArray = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,1],
    [1,1,1,0,1,1,0,1,1,1,1,1,1,0,0,1,0,0,0,1],
    [1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1],
    [1,1,1,0,1,1,0,0,0,1,1,1,1,0,1,1,0,0,0,1],
    [1,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1,0,1,1,1],
    [2,0,0,0,1,0,0,0,0,1,1,0,1,1,1,1,0,1,1,1],
    [1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,0,0,1],
    [1,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1],
]

const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');

const squareSide = 50;

function drawField(){
        for (let i = 0; i < squareArray.length; i++){
            for (let j = 0; j < squareArray[i].length; j++){
                let x = j * squareSide;
                let y = i * squareSide;
    
                let cellColor = 'white';
    
                if(squareArray[i][j] === 1){
                    cellColor = 'black';
                }
                else if(squareArray[i][j] === 2){
                    cellColor = 'green';
                }
                else if(squareArray[i][j] === 3){
                    cellColor = 'red';
                }
                
                ctx.beginPath();
                ctx.fillStyle = cellColor;
                ctx.fillRect(x,y,squareSide,squareSide);
            }
        }
    }

drawField();


