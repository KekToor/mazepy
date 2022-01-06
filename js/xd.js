const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');

        ctx.beginPath();
        ctx.lineWidth = "6";
        ctx.fillStyle = "red"
        ctx.fillRect(0,480,80,80);
        ctx.fillStyle = 'black';
        ctx.fillRect(0,0,160,240);
        ctx.fillRect(0,240,320,240);
        ctx.fillRect(120,0,480,40)
        ctx.fillRect(0,560,400,500);
        ctx.fillRect(400,600,120,-440);
        ctx.fillRect(520,160,-280,-40);
        ctx.fillRect(520,260,300,60);
        ctx.fillRect(600,0,80,180);
        ctx.fillRect(760,260,60,-170);
        ctx.fillRect(0,0,1000,10);
        ctx.fillRect(900,0,100,400);
        ctx.fillRect(1000,400,-400,100);
        ctx.fillRect(520,580,480,20);
        ctx.fillStyle = "green";
        ctx.fillRect(1000,580,-80,-80)
        ctx.stroke();

        class Rectangle {
            static DEFAULT_SIZE = 40;
            static FILL_COLOR = 'black';
            static STROKE_COLOR = 'red';
            static FRICTION = 0.9;
        
            constructor(x, y, speed = 3) {
                this.x = x;
                this.y = y;
                this.velX = 0;
                this.velY = 0;
                this.angle = 0;
                this.size = Square.DEFAULT_SIZE;
                this.speed = speed;
                this.color = Square.FILL_COLOR;
                this.active = false;
                this.friction = Square.FRICTION;
                this.keys = [];
            }
        
            detectCursor(curX, curY) {        
                return (curX >= this.x && curX <= this.x + this.size) && (curY >= this.y && curY <= this.y + this.size);
            }
        
            move() {
                if (this.keys['KeyW']) {
                    if (this.velY > -this.speed) {
                        this.velY--;
                    }
                }
                
                if (this.keys['KeyS']) {
                    if (this.velY < this.speed) {
                        this.velY++;
                    }
                }
        
                if (this.keys['KeyD']) {
                    if (this.velX < this.speed) {
                        this.velX++;
                    }
                }
                if (this.keys['KeyA']) {
                    if (this.velX > -this.speed) {
                        this.velX--;
                    }
                }
            
                this.velY *= this.friction;
                this.y += this.velY;
                this.velX *= this.friction;
                this.x += this.velX; 
        
                if (this.x > canvas.width - this.size) {
                    this.x = canvas.width - this.size;
                    this.velX = -this.velX;
                } 
                
                if (this.x < 0) {
                    this.x = 0;
                    this.velX = -this.velX;
                }
        
                if (this.y > canvas.height - this.size) {
                    this.y = canvas.height - this.size;
                    this.velY = -this.velY;
                } 
                
                if (this.y < 0) {
                    this.y = 0;
                    this.velY = -this.velY;
                }
            }
          
            ;
        
        
            draw() {        
                ctx.translate(this.x  + this.size / 2, this.y  + this.size / 2);
                ctx.rotate((this.angle / 360) * Math.PI * 2);
                ctx.translate(-(this.x  + this.size / 2), -(this.y + this.size / 2));            
                ctx.fillStyle = this.color;
                ctx.fillRect(this.x, this.y, this.size, this.size);
                if (this.active) {
                    ctx.beginPath();
                    ctx.strokeStyle = Square.STROKE_COLOR;
                    ctx.lineWidth = 5;
                    ctx.strokeRect(this.x, this.y, this.size, this.size);
                    ctx.closePath();
                }
                ctx.setTransform(1, 0, 0, 1, 0, 0);
            }
        }

        class Game{

        }