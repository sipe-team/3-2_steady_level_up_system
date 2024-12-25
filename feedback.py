from openai import OpenAI
import requests
import sys
import re
import os
import argparse
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("GPT_KEY"),
)


def summarize_content(content):
    prompt = "공부한 내용에 대해서 피드백을 해줘. 공부한 내용에 보충을 해도 되고, 더 공부하기 좋은 내용을 추천해줘  :\n\n" + content
    try:
        # ChatCompletion API 호출
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        # 응답에서 요약 텍스트 추출
        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        print(f"Error summarizing content: {e}")
        return "Summary could not be generated."


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process file content.")
    parser.add_argument("--content", required=True,
                        help="The content of the file to process.")

    # Parse the arguments
    args = parser.parse_args()
    content = args.content

    if content:
        clean_content = re.sub(r'<[^>]+>', '', content)
        summary = summarize_content(clean_content)
        print(summary)
    else:
        print("No content to summarize.")
