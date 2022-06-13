#!/usr/bin/env python3


from .emoji_remover import remove_emojis


def test_remove_emojis():
    assert remove_emojis("🎒Nicovita") == "Nicovita"
    assert remove_emojis("❌Cancelar") == "Cancelar"
    assert remove_emojis("⭕️Abierto") == "Abierto"
    assert remove_emojis("🔴Cerrado") == "Cerrado"
