<!doctype html>
<html>
    <head>
        <title>Order a Melongram</title>
    </head>
    <body>
        <header>
            <h1>Order a Melongram</h1>
        </header>
        <section id="intro">
            <p>There's no better way to show a loved one you care than with a Melongram.</p>

            <p>Each Melongram comes with a custom message printed on high-quality cardstock
                and your choice of a hand-picked, premium melon.</p>
        </section>

        <section id="melon-options">
            <h2>Melon Options</h2>

            <p>Choose from one of these melons:</p>
            
            <table>
                <tr><td>Watermelon</td> <td>$1,200.00</td></tr>
                <tr><td>Canteloupe</td> <td>$400.00</td></tr>
                <tr><td>Honeydew</td> <td>$1,750.00</td></tr>
            </table>
        </section>

        <section id="order-form">
            <h2>Order Form</h2>
            <form>
                <div class="username">
                    <label for="user-name">Your name</label>
                    <input type="text" name="name" id="user-name">
                </div>
                
                <div class="recipient-name">
                    <label for="recipient">Who are we sending this to?</label>
                    <input type="text" name="recipient" id="recipient">
                </div>

                <div class="melon">
                    <label for="melon-table">Choose a melon</label>
                    <select name="melon" id="melon-table">
                        <option value="watermelon">Watermelon</option>
                        <option value="cantaloupe">Canteloupe</option>
                        <option value="honeydew">Honeydew</option>
                    </select>
                </div>

                <div class="delivery">
                    <fieldset>
                        <legend>When should we deliver?</legend>

                        <input type="radio" name="time" value="am" id="am">
                        <label for="am">Morning</label>
                        <input type="radio" name="time" value="pm" id="pm">
                        <label for="pm">Evening</label>
                        <input type="radio" name="time" value="any" id="any">
                        <label for="any">Any time</label>
                    </fieldset>
                </div>

                <div class="message">
                    <p><label for="text-message">Enter your message:</label></p> 
                    <textarea name="message" id="text-message"></textarea>
                </div>

                <div class="subscribe">
                    <fieldset>
                        <legend> Subscribe to our newsletter</legend>
                        <label for="newsletter-subscribe">Yes</label>
                        <input type="checkbox" name="subscribe" value="yes" id="newsletter-subscribe">
                    </fieldset>
                </div>

                <button type="submit">Submit</button>
            </form>
        </section>
    </body>
</html>
