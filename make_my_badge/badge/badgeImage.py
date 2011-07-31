#
#  Copyright (c) 2007 Silver Stripe Software Pvt Ltd
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
#
#
#  Contributions and bug reports are welcome. Send an email to
#  siddharta at silverstripesoftware dot com
#

from PIL import Image, ImageDraw, ImageFont
import os

#####################################################
######## User Defined Values ########################
#####################################################
NAME_COLOR = "#000000"
COMPANY_COLOR = "#ee3622"
ID_COLOR = "#000000"
FOLD_COLOR = "#000000"


class BadgeImage(object):
    def __init__(self, filename, font_path, name_color=None, company_color=None):
        self.img = Image.open(filename)
        self.draw = ImageDraw.Draw(self.img)
        self.width = int(self.img.size[0]*0.9)
        self.name_color =  name_color if name_color else NAME_COLOR
        self.company_color =  name_color if company_color else COMPANY_COLOR
        self.font_path = font_path

    def getFont(self, size):
        try:
            font_path = os.path.join(self.font_path, "Fontin-Bold.otf")
            font = ImageFont.truetype(font_path, size*300/72)
            return font
        except IOError:
            return ImageFont.load_default()
        
    def drawAlignedText(self, pos, text, (font, color), xtransform, ytransform):
        width,height = font.getsize(text)
        xpos = xtransform(pos[0], width)
        ypos = ytransform(pos[1], height)
        self.draw.text((xpos, ypos), text, fill=color, font=font)

    def drawCenteredText(self, pos, text, font):
        self.drawAlignedText(pos, text, font, lambda x,w:x-w/2, lambda y,h:y-h/2)

    def getFitSize(self, startsize, text):
        size = startsize
        font = self.getFont(size)
        textwidth, textheight = font.getsize(text)
        while textwidth > self.width:
            size -= 1
            font = self.getFont(size)
            textwidth, textheight = font.getsize(text)
        return size

    def drawPerson(self, name):
        linepos = (self.width/2, 240)
        line1pos = (self.width/2, 150)
        line2pos = (self.width/2, 320)
        if name.find(" ") >= 0:
            firstname, rest = name.split(" ", 1)
        else:
            firstname, rest = (name, "")
        if rest != "":
<<<<<<< HEAD
            personFont = self.getFont(self.getFitSize(45, firstname))
            self.drawCenteredText(line1pos, firstname, (personFont, NAME_COLOR))
            personFont = self.getFont(self.getFitSize(45, rest))
            self.drawCenteredText(line2pos, rest, (personFont, NAME_COLOR))
        else:
            personFont = self.getFont(self.getFitSize(45, name))
            self.drawCenteredText(linepos, name, (personFont, NAME_COLOR))

    def drawCompany(self, name):
        pos = (self.width/2, 500)
        font = self.getFont(self.getFitSize(26, name))
        self.drawCenteredText(pos, name, (font, COMPANY_COLOR))

    def drawId(self, id):
        pos = (50, 50)
        font = self.getFont(8)
        self.drawCenteredText(pos, id, (font, ID_COLOR))
=======
            personFont = ImageFont.truetype("Trebucbd.ttf", self.getFitSize(45, firstname)*300/72)
            self.drawCenteredText(line1pos, firstname, (personFont, self.name_color))
            personFont = ImageFont.truetype("Trebucbd.ttf", self.getFitSize(45, rest)*300/72)
            self.drawCenteredText(line2pos, rest, (personFont, self.name_color))
        else:
            personFont = ImageFont.truetype("Trebucbd.ttf", self.getFitSize(45, name)*300/72)
            self.drawCenteredText(linepos, name, (personFont, self.name_color))

    def drawCompany(self, name):
        pos = (self.width/2, 500)
        font = ImageFont.truetype("Trebucbd.ttf", self.getFitSize(26, name)*300/72)
        self.drawCenteredText(pos, name, (font, self.company_color))

    def drawId(self, id):
        pos = (50, 50)
        font = ImageFont.truetype("Trebucbd.ttf", 8*300/72)
        self.drawCenteredText(pos, id, (font, self.name_color))
>>>>>>> 212d6e2de8435240139f2cf7f701ace1dffc084a


    def save(self, filename, doubleSided=False):
        if not doubleSided:
            self.img.save(filename)
            return

        newimg = Image.new("RGB", (self.img.size[0]*2+20, self.img.size[1]), FOLD_COLOR)
        newimg.paste(self.img, (0,0))
        newimg.paste(self.img, (self.img.size[0]+20,0))
        newimg.save(filename)
