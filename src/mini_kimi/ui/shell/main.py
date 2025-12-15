import sys
import os

# 确保能导入 mini_kimi 包
# 在实际项目中，这通常通过安装包或设置 PYTHONPATH 来解决
# 这里为了简单，我们动态添加 src 目录到 sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
# current: src/mini_kimi/ui/shell
# need: src
src_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.insert(0, src_dir)

from mini_kimi.soul.soul import Soul

def main():
    print("Welcome to Mini Kimi CLI (Refactored)!")
    print("Type 'exit' or 'quit' to leave.\n")
    
    agent = Soul()

    while True:
        try:
            user_input = input("\n\033[1;36mUser>\033[0m ")
            if user_input.lower() in ["exit", "quit"]:
                break
            if not user_input.strip():
                continue
                
            agent.run(user_input)
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

