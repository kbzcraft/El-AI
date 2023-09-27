from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
import warnings
warnings.simplefilter("ignore")

###################################

url = "https://www.semrush.com/goodcontent/summary-generator/"

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
# chrome_options.add_argument("--use-fake-ui-for-media-stream") #Allows microphone ascess
# chrome_options.add_argument("--use-fake-device-for-media-stream")
chrome_options.add_argument("--headless=new")
# chrome_options.add_experimental_option("detach", True)
# chrome_options.headless=False
print("opening the browser")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(url)
# sleep(.5)
paragraphXpath = "/html/body/div[1]/main/div/div/div[3]/div/div[1]/div[2]/div/div[2]/div/cmp-summary-generator-form/div/div/div/div[1]/div[1]/div/button[1]"
bulletPointXpath = "/html/body/div[1]/main/div/div/div[3]/div/div[1]/div[2]/div/div[2]/div/cmp-summary-generator-form/div/div/div/div[1]/div[1]/div/button[2]"
textAreaXpath= "/html/body/div[1]/main/div/div/div[3]/div/div[1]/div[2]/div/div[2]/div/cmp-summary-generator-form/div/div/div/div[2]/form/div/div/textarea"
summaryXpath = "/html/body/div[1]/main/div/div/div[3]/div/div[1]/div[2]/div/div[2]/div/cmp-summary-generator-form/div/div/div/div[2]/div/div/div"
generateButtonXpath="/html/body/div[1]/main/div/div/div[3]/div/div[1]/div[2]/div/div[2]/div/cmp-summary-generator-form/div/div/div/div[2]/form/button"
shortSummaryOptionXpath = "/html/body/div[1]/main/div/div/div[3]/div/div[1]/div[2]/div/div[2]/div/cmp-summary-generator-form/div/div/div/div[1]/div[2]/div[2]/span[1]"

paragraphOption = driver.find_element(By.XPATH,paragraphXpath)
bulletPointOptions = driver.find_element(By.XPATH,bulletPointXpath)
textArea = driver.find_element(By.XPATH,textAreaXpath)
summary=driver.find_element(By.XPATH,summaryXpath)
generateBtn = driver.find_element(By.XPATH,generateButtonXpath)
shortSummary = driver.find_element(By.XPATH,shortSummaryOptionXpath)

# Find the element you want to scroll to by its id
element_to_scroll_to = driver.find_element(by=By.ID,value="input")
# Use JavaScript to scroll to the element
driver.execute_script("arguments[0].scrollIntoView();", element_to_scroll_to)

data = """The law of demand is a fundamental principle in economics that describes the relationship between the price of a good or service and the quantity demanded by consumers. It can be summarized as follows:

The law of demand states that, all else being equal, as the price of a good or service decreases, the quantity demanded for that good or service increases. Conversely, as the price of a good or service increases, the quantity demanded decreases.

Key points about the law of demand:

Inverse Relationship: The law of demand implies an inverse relationship between price and quantity demanded. When the price goes down, people tend to buy more of a product, and when the price goes up, they tend to buy less.

Ceteris Paribus: The phrase "all else being equal" (ceteris paribus in Latin) is important in understanding this law. It means that the law of demand assumes that other factors influencing demand, such as consumer income, preferences, and the prices of related goods, remain constant. If any of these factors change, it can influence demand independently of the price.

Slope: When the relationship between price and quantity demanded is plotted on a graph, it typically shows a downward-sloping demand curve. This curve illustrates that as you move along the curve, either increasing or decreasing the price, the quantity demanded changes in the opposite direction.

Utility and Marginal Utility: The law of demand is often explained by the concept of diminishing marginal utility. As consumers purchase more of a product, the additional satisfaction or utility they derive from each additional unit (marginal utility) tends to decrease. This means that consumers are willing to pay less for each additional unit, leading to a lower price and higher quantity demanded.

Market Behavior: The law of demand has important implications for market behavior. In a competitive market, when the price of a good is too high, there will be excess supply (surplus), and when the price is too low, there will be excess demand (shortage). Prices tend to adjust to reach an equilibrium where supply equals demand.

Overall, the law of demand is a fundamental concept in economics that helps explain how consumers make choices in response to changes in prices, and it plays a central role in understanding market dynamics and pricing strategies."""
textArea.send_keys(data)
action = ActionChains(driver)
# shortSummary.click()
action.click(on_element = shortSummary)
action.perform()

action.click(on_element = generateBtn)
action.perform()
# while True:
#     if summary.is_displayed:
#         summary = summary.text
#         if summary !=" " and len(summary) !=0:
#             print(summary)
#             break
#         else:
#             continue
#     else:
#         continue



# Wait until the element containing the summarized text is not empty
wait = WebDriverWait(driver, 10)
summary_element = wait.until(lambda driver: driver.find_element(By.XPATH,summaryXpath).text.strip() != "")

# Get the summarized text
summarized_text = summary_element.text

# Now you can copy the summarized text or perform any other desired actions with it
print("Summarized Text:", summarized_text)

# Close the browser window
driver.quit()