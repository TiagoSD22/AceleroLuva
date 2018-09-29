# AceleroLuva
Luva feita com arduino pro mini e sensor acelerômetro

Este projeto feito com arduino pro mini se constitui em uma luva com sensor acelerômetro que pode ser usado como um dispositivo
HID com interação com pc. Ao movimentar a luva o sensor acelerômetro envia sinais para o arduino que é capaz de reconhecer a 
direção dos movimentos feitos e interpretá-los para interagir com um pc. Os comandos do arduino são enviados via bluetooth
que podem ser recebidos pelo pc a partir de um módulo bluetooth e um adaptador serial - usb conectado à porta usb do computador.
Para configurar atalhos de teclado aos comandos enviados pela luva há uma aplicação com interface gráfica feita em python e
usando o módulo pySerial que permite usar a luva para controlar com comandos simples o computador. Bom para jogos 2D é possível
fazer movimentos como andar, mover para direita, pular, etc.. apenas com movimentos da mão. A luva é alimenta por 3 pilhas AA
em série que ficam na base do pulso fornecendo cerca de 4.5V para ligar o MCU arduino pro mini, o sensor acelerômetro MMA7361,
módulo bluetooth HC05 e led de funcionamento.
