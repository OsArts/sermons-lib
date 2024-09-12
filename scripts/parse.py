# 2024-09-09 06:31
# /Users/dwarf/Projects/sermons-lib/scripts/parse.py

from bs4 import BeautifulSoup
import requests

# sermons21.htm
# url = ("http://sdaprotvino.ru/"
        # "sermons21.htm")

# html = requests.get(url).text
html = """
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/311222.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 31.12.2022 <span style="color: red;">"Путь, истина и жизнь</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>(<a href="sermonsHD/311222.mp4">HD MP4</a>, 36 мин., 557 МБ). <a href="sermons/311222.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/241222.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 24.12.2022 <span style="color: red;">"Здесь терпение святых</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/241222.mp4">HD MP4</a>, 57 мин., 898 МБ). <a href="sermons/241222.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/101222.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 10.12.2022 <span style="color: red;">"Кто мой ближний?</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/101222.mp4">HD MP4</a>, 44 мин., 697 МБ). <a href="sermons/101222.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/031222.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 03.12.2022 <span style="color: red;">"Что есть истина?</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/031222.mp4">HD MP4</a>, 40 мин., 630 МБ). <a href="sermons/031222.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/261122.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 26.11.2022 <span style="color: red;">"Надежда в Библии</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/261122.mp4">HD MP4</a>, 42 мин., 654 МБ). <a href="sermons/261122.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/191122.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 19.11.2022 <span style="color: red;">"Не заботьтесь о завтрашнем дне</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/191122.mp4">HD MP4</a>, 45 мин., 699 МБ). <a href="sermons/191122.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/121122.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 12.11.2022 <span style="color: red;">"Иеффай</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/121122.mp4">HD MP4</a>, 61 мин., 951 МБ). <a href="sermons/121122.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/051122.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 05.11.2022 <span style="color: red;">"Хождение по воде</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/051122.mp4">HD MP4</a>, 24 мин., 383 МБ). <a href="sermons/051122.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/291022.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 29.10.2022 <span style="color: red;">"Слово в Псалме 118</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/291022.mp4">HD MP4</a>, 34 мин., 537 МБ). <a href="sermons/291022.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/221022_creationsabbath.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Служение Субботы Творения 22.10.2022<span style="color: red;"></span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;"><span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/221022_creationsabbath.mp4">HD MP4</a>, 92 мин., 1.41 ГБ).<a href="sermons/151022.mp3"><br>
</a></strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/151022.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 15.10.2022 <span style="color: red;">"Вернейшее пророческое слово</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/151022.mp4">HD MP4</a>, 43 мин., 675 МБ). <a href="sermons/151022.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/081022.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 08.10.2022 <span style="color: red;">"Время кризиса</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/081022.mp4">HD MP4</a>, 40 мин., 633 МБ). <a href="sermons/081022.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/011022.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 01.10.2022 <span style="color: red;">"Примирение с Богом</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;"></span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/011022.mp4">HD MP4</a>, 37 мин., 575 МБ). <a href="sermons/011022.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/240922.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 24.09.2022 <span style="color: red;">"Пшеница и плевелы</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;"></span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/240922.mp4">HD MP4</a>, 45 мин., 711 МБ). <a href="sermons/240922.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/170922.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 17.09.2022 <span style="color: red;">"Если Бог за нас, кто против нас?</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;"></span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/170922.mp4">HD MP4</a>, 49 мин., 770 МБ). <a href="sermons/170922.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/100922.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 10.09.2022 <span style="color: red;">"Взаимопонимание</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;"></span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/100922.mp4">HD MP4</a>, 45 мин., 712 МБ). <a href="sermons/100922.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/030922.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 03.09.2022 <span style="color: red;">"Пожелания учащимся</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;"></span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/030922.mp4">HD MP4</a>, 37 мин., 585 МБ). <a href="sermons/030922.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/270822.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 27.08.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">Почему мы приходим в церковь?</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/270822.mp4">HD MP4</a>, 57 мин., 887 МБ). <a href="sermons/270822.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/200822.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 20.08.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">Не бойся, ибо Я - с тобою</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/200822.mp4">HD MP4</a>, 47 мин., 735 МБ). <a href="sermons/200822.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/130822.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 13.08.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">Убежище в Боге</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/130822.mp4">HD MP4</a>, 44 мин., 691 МБ). <a href="sermons/130822.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/060822.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 06.08.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">Не произноси имени Господа напрасно</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/060822.mp4">HD MP4</a>, 43 мин., 671 МБ). <a href="sermons/060822.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/300722.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 30.07.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">Меч Господа и Гедеона</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/300722.mp4">HD MP4</a>, 47 мин., 735 МБ). <a href="sermons/300722.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/230722.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 23.07.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">Два поприща</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/230722.mp4">HD MP4</a>, 44 мин., 689 МБ). <a href="sermons/230722.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/090722.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 09.07.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">Соблюдающие заповеди Божии и веру в Иисуса</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/090722.mp4">HD MP4</a>, 47 мин., 733 МБ). <a href="sermons/090722.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/250622.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 25.06.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">И прости нам долги наши, как и мы прощаем должникам нашим</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/250622.mp4">HD MP4</a>, 28 мин., 440 МБ). <a href="sermons/250622.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/180622.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 18.06.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">Уроки книги Исход 17 гл.</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/180622.mp4">HD MP4</a>, 36 мин., 562 МБ). <a href="sermons/180622.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/110622.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 11.06.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">Героини веры</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/110622.mp4">HD MP4</a>, 29 мин., 452 МБ). <a href="sermons/110622.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/040622.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 04.06.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">Библейская модель евангелизации</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/040622.mp4">HD MP4</a>, 36 мин., 567 МБ). <a href="sermons/040622.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/280522.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 28.05.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">Четыре обмана дьявола</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/280522.mp4">HD MP4</a>, 30 мин., 468 МБ). <a href="sermons/280522.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/210522.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 21.05.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">Милость</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/210522.mp4">HD MP4</a>, 50 мин., 782 МБ). <a href="sermons/210522.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/140522.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 14.05.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">Почему Бог допускает испытания</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/140522.mp4">HD MP4</a>, 24 мин., 371 МБ). <a href="sermons/140522.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/070522.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 07.05.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">Дар благодати</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/070522.mp4">HD MP4</a>, 50 мин., 788 МБ). <a href="sermons/070522.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/300422.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 30.04.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">Побеждающая любовь Божья</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/300422.mp4">HD MP4</a>, 33 мин., 522 МБ). <a href="sermons/300422.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/230422.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 23.04.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">Удивительное пророчество Иезекииля</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/230422.mp4">HD MP4</a>, 53 мин., 835 МБ). <a href="sermons/230422.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/160422.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 16.04.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">О Духе Святом</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/160422.mp4">HD MP4</a>, 52 мин., 820 МБ). <a href="sermons/160422.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/090422.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 09.04.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">Вы - соль земли</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/090422.mp4">HD MP4</a>, 36 мин., 568 МБ). <a href="sermons/090422.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/020422.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 02.04.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">На что уходит наше время?</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/020422.mp4">HD MP4</a>, 29 мин., 450 МБ). <a href="sermons/020422.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/260322.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 26.03.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">На Вечерю Господню</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/260322.mp4">HD MP4</a>, 23 мин., 367 МБ). <a href="sermons/260322.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/190322.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 19.03.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">Молитва последнего времени</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/190322.mp4">HD MP4</a>, 41 мин., 647 МБ). <a href="sermons/190322.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/120322.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 12.03.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">Беседа Христа с самарянкой</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/120322.mp4">HD MP4</a>, 38 мин., 599 МБ). <a href="sermons/120322.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/050322.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 05.03.2022 <span style="color: red;">"</span></span></strong></span></strong><span style="font-size: 11pt; font-family: &quot;Calibri&quot;,sans-serif; font-weight: bold; color: red;"></span><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">Господи! спаси нас: погибаем</span></span></strong></span></strong><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><span style="color: red;">"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/050322.mp4">HD MP4</a>, 27 мин., 425 МБ). <a href="sermons/050322.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/260222.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 26.02.2022 <span style="color: red;">"Свобода от беспокойства"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/260222.mp4">HD MP4</a>, 25 мин., 394 МБ). <a href="sermons/260222.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/190222.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 19.02.2022 <span style="color: red;">"О зависти"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/190222.mp4">HD MP4</a>, 29 мин., 459 МБ). <a href="sermons/190222.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/120222.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 12.02.2022 <span style="color: red;">"Божий институт семьи под угрозой"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/120222.mp4">HD MP4</a>, 57 мин., 899 МБ). <a href="sermons/120222.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/050222.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 05.02.2022 <span style="color: red;">"Молитва преображения"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/050222.mp4">HD MP4</a>, 25 мин., 388 МБ). <a href="sermons/050222.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/290122.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 29.01.2022 <span style="color: red;">"Да приидет Царствие Твое"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/290122.mp4">HD MP4</a>, 44 мин., 685 МБ). <a href="sermons/290122.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/220122.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 22.01.2022 <span style="color: red;">"Берегитесь, чтобы кто не прельстил вас"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/220122.mp4">HD MP4</a>, 28 мин., 442 МБ). <a href="sermons/220122.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/150122.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 15.01.2022 <span style="color: red;">"Великие пророчества Христа в Мф. 24"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/150122.mp4">HD MP4</a>, 31 мин., 485 МБ). <a href="sermons/150122.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/080122.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 08.01.2022 <span style="color: red;">"Рождество Христово"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/080122.mp4">HD MP4</a>, 28 мин., 436 МБ). <a href="sermons/080122.mp3">Аудио МР3</a>.</strong></td>
          </tr>
          <tr>
            <td style="vertical-align: top;"><br>
            </td>
            <td style="vertical-align: top;"><br>
            </td>
          </tr>
<tr>
            <td style="vertical-align: top; text-align: center;"><a href="sermonsHD/010122.mp4"><img style="border: 0px solid ; width: 50px; height: 48px;" src="images/sdalogo1.gif" alt=""></a></td>
            <td style="vertical-align: top;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;"><strong><span style="font-size: medium;" data-mce-style="font-size: medium;">Проповедь 01.01.2022 <span style="color: red;">"Истинная вера"<span style="color: rgb(0, 0, 153);"></span></span><span style="color: rgb(255, 0, 0);" data-mce-style="color: #ff0000;"></span></span></strong></span><br>
(<a href="sermonsHD/010122.mp4">HD MP4</a>, 55 мин., 856 МБ). <a href="sermons/010122.mp3">Аудио МР3</a>.</strong></td>
          </tr>

"""
# http://sdaprotvino.ru/sermons21.htm

soup = BeautifulSoup(html, 'html5lib')

# red_title = soup.find('span', 'style': {"color: red;"}).text
# red_title = soup.find('td').text
red_title = soup.find_all('span', {'style': 'color: red;'})

# create list which has content Titles
titles = [span.get_text() for span in red_title]

# Coleect the titles from list
title_result = []
for title in titles:
    m = re.search(r'(")')

print(red_title)