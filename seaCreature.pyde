from random import choice, randint

def pCreature(tSize, step, sca, offset):
    for i in range(0,tSize + step, step):
        for j in range(0, tSize + step, step):
            x = round(map(noise(i*sca, j*sca), 0, 1, -offset, offset))
            y = round(map(noise(j*sca, i*sca), 0, 1, -offset, offset))
            point(x,y)
            

def setup():
    size(1000,1000)
    background(0)
    strokeWeight(1)
    blendMode(ADD)
    noiseDetail(3)
    stroke(15)
    
    # background noise effect
    pushMatrix()
    translate(width/2 + 100, height/2 + 100)
    pCreature(1000, 1, 0.3, 1000)
    popMatrix()
    
    noiseDetail(10)
    stroke(50)
    
    # noise seeds for pCreatures
    a = int(random(1000000))
    b = int(random(1000000))
    c = int(random(1000000))
    d = int(random(1000000))
    e = int(random(1000000))
    
    # pCreature generation
    pushMatrix()
    translate(width/2, height/2)
    noiseSeed(a)
    pCreature(250, 1, 0.003, 550)
    noiseSeed(b)
    pCreature(250, 1, 0.003, 550)
    noiseSeed(c)
    pCreature(250, 1, 0.003, 550)
    noiseSeed(d)
    pCreature(250, 1, 0.003, 550)
    noiseSeed(e)
    pCreature(250, 1, 0.003, 550)
    popMatrix()
    
    ## Text Generation ##
    textSize(14)
    fill(255)
    
    save("seaCreature.png")
