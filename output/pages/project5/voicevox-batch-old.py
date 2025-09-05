import asyncio
import glob
import os
import time

from pydub import AudioSegment, effects

# ライブラリのインストール
# pip install voicevox-client
from voicevox import Client

# Dockerコンテナの起動
"""
docker pull voicevox/voicevox_engine:nvidia-ubuntu20.04-latest
docker run --rm --gpus all -p '127.0.0.1:50021:50021' voicevox/voicevox_engine:nvidia-ubuntu20.04-latest
"""

file_directory = r"C:\Users\XXX\Desktop\files"
speaker_id = 14


async def main():
    async with Client() as client:
        files = sorted(glob.glob(os.path.join(file_directory, "*.txt")))
        for i, file in enumerate(files, 1):
            print(file)
            f = open(file, "r", encoding="UTF-8")
            text = f.read()
            sentences = text.replace("。", "。\n").split("\n")

            t1 = time.time()
            concatenated = AudioSegment.empty()
            for a, sentence in enumerate(sentences):
                if sentence == "":
                    continue

                audio_query = await client.create_audio_query(sentence, speaker_id)
                audio = await audio_query.synthesis(speaker=speaker_id)
                concatenated += AudioSegment(audio)
                concatenated += AudioSegment.silent(duration=500)  # 0.5秒の無音追加

            t2 = time.time()
            elapsed_time = t2 - t1
            print(f"所要時間：{elapsed_time}")

            # 出力
            concatenated = effects.normalize(concatenated)  # ノーマライズ
            concatenated = effects.speedup(concatenated, playback_speed=1.5)  # 速度調整
            concatenated.export(
                os.path.join(
                    file_directory, f"{os.path.basename(file).split('.')[0]}.mp3"
                ),
                format="mp3",
                bitrate="192k",
            )


if __name__ == "__main__":
    asyncio.run(main())
