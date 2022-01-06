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

class Square{
    static DEFAULT_SIZE = 50;

    constructor(x,y,color,gridX,gridY){
        this.x = x;
        this.y = y;
        this.color = color;
        this.size = Square.DEFAULT_SIZE;
        this.gridX = gridX;
        this.gridY = gridY;
    }

    draw(){
        ctx.fillStyle = this.color;
        ctx.fillRect(this.x,this.y,this.size,this.size);
    }
}

class Grid{
    static COLORS = ['white','black','green','red'];
    constructor(width,height){
        this.width = width;
        this.height = height;
        this.squares = [];
        for (let i = 0; i < this.width; i++){
            for (let j = 0; j < this.height; j++){
                this.squares.push(new Square(i * Square.DEFAULT_SIZE,j * Square.DEFAULT_SIZE, Grid.COLORS[squareArray[j][i]], j,i));
            }
        }
    }


    draw(){
        this.squares.forEach(function(square,index,array){
            square.draw();
        });

    }
}




class Game{
    constructor(){
        this.grid = new Grid(squareArray[0].length,squareArray.length);
        console.log(this.grid);
    }

    draw(){
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        this.grid.draw();
    }
   

    play() {
        requestAnimationFrame(animate); 
    }
    
}

function animate() {
    requestAnimationFrame(animate);
    game.draw();    
}

let game = new Game();

game.play();

//Vyzkoušet - předávat pole z jiného souboru