# List Prioritisation Using AHP (Analytic Hierarchy Process)

### [🚀 **Live Demo** ](https://pro-planner-07d8f7f68403.herokuapp.com/)

## Overview

This project provides a web-based tool to prioritise a list of items using the Analytic Hierarchy Process (AHP). AHP is a structured technique for organising and analysing complex decisions, which involves breaking down a problem into a hierarchy, comparing the elements pairwise, and synthesising the results to determine priorities. This web app demonstrates this in a simplified process, allowing users to rank a given set of items based on their preference efficiently.

## Features

- AHP Pairwise Comparisons: The tool performs pairwise comparisons of items to derive priority scores.
- Randomise Items: Randomly shuffle items of a random category to introduce objectivity in decision-making.
- Item Ranking Interface: Drag-and-drop interface to reorder tasks by preference.
- Dark Mode: Toggle between light and dark modes for a better user experience.

## Interact with the Tool:

Reorder Tasks: Drag and drop tasks in the list to reorder them.
Rank by Preference: Click on "Order" to start the AHP ranking process. You will be presented with pairs of items to choose between. The system will automatically calculate the most prioritised task based on your selections.

## How It Works

- Pairwise Comparisons: The AHP algorithm prompts the user to compare items two at a time, asking which one is more important. Based on these comparisons, it assigns a score to each item.
- Item Ranking: After completing the comparisons, items are ranked according to their cumulative scores, reflecting their priority.

## Technologies Used

- **HTML/CSS:** For structuring and styling the user interface.
- **Bootstrap:** For responsive design and UI components.
- **JavaScript:** To handle user interactions and implement the AHP algorithm.
- **Python:** Handles the backend logic and processing.
- **Django:** The web application framework utilised to organise and manage the backend code.
- **PostgreSQL:** Database option used for data storage and information retrieval.
- **Heroku:** The app is configured for deployment on Heroku, as configured by the a Procfile.

## License

This work is licensed under Attribution-NonCommercial 4.0 International. See the [LICENSE](https://github.com/negin-mgdm/ahp-prioritiser/blob/master/LICENSE.md) file for details.

## Resources

AHP Method Overview: [Learn more about AHP](https://www.indeed.com/career-advice/career-development/ahp-method)

## Contact

For any questions or issues, please [contact me](https://github.com/negin-mgdm).
