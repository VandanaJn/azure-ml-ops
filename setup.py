from setuptools import setup

setup(name="summarize",
      description="cli to summarize a url or file",
      author="Vandana",
      package_dir={"": "scripts"},
      py_modules=["summarize","extract_text"],
      install_requires=["transformers==4.37.2",
        "huggingface_hub",
        "beautifulsoup4",
        "click","torch"],
      entry_points={
            "console_scripts": [
                "summarize=summarize:summarize" ,
                "extract_text=extract_text:extract_text" 
            ]},
      python_requires=">=3.11"
    )