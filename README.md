# IT_encoder
PSCP project - IT_encoder

**Website:** 

https://anawina.github.io/IT_encoder/

**Desktop_app:** run "main view.py" 

by Pywebview

## IT_encoder คืออะไร?
ปกติแล้วในวิชา MFIT เราจะเรียนเรื่อง matrix ซึ่งอาจจะยากสำหรับนศ.ที่ไม่เคยเรียนมาก่อน โดยเฉพาะการเข้ารหัสข้อความ โดยจะนำข้อความมาแปลงเป็นลำดังตัวอักษรภาษาอังกฤษ a = 1 z =26 เป็นต้นแล้วจะนำกุญแจที่เป็นเมทริกซ์มาคูณ ส่วนการถอดรหัสก็จะนำกุญแจมาหา inverse แล้วก็คูณกับ matrix ที่เข้ารหัส จะได้เป็นข้อความเดิมออกมา ก็เลยจะทำสิ่งนี้ขึ้นเพื่อให้เข้าใจในเรื่อง matrix มากขึ้น เข้าใจการเขียนโปรแแกรม เข้าใจลำดับการทำงาน และ สะดวกในการเข้ารหัสถอดรหัสไปใช้ในกิจกรรมอื่นๆอีกด้วย แต่ว่าก็จะมีเพิ่มอัลกอลิทึมอื่นๆอีกให้มีการเข้ารหัส ถอดรหัส ที่หลากหลายแนว เช่น base64 ascii url utf-8 โดยจะใช้ import เท่าที่จำเป็น เพื่อให้เราเข้าใจกระบวนการเข้ารหัสอย่างลึกซึ้งถึงแก่น

## Including
### Binary
* base64
* base32
* Hex/base16

### iJudge
* mealEncoding
* numberFactory
* runLength
* shorten

### Text
* upper/lowercase
* swapcase
* capitalize
* title
* join/split-text

### Advanced
* Matrix Cryptography - numpy

## on Development 
* ROT13
* Morse code
* ascii
* ... (more information soon)

## Credits
67070197 นายอภิพล สุวรรณชัยสกุล

67070196 นายอนาวิล ภู่รัตนากรกุล

67070303 คทาฤทธี อวยพร

67070162 นายวสวัตติ์ เนตร์พันธ์

67070184 น.ส.สิทธารถ สีโยธะ


### Powered by HTML CSS JS & Python

.Brython
```py
document["translateBtn"].bind("click", translate)
```

<py-script>

```py
Element("encoded_output").write(encoded)
```




