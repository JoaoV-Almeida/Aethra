PERSONAS = {

    "executive": {
        "label": "🏢 Executive / Business Pro",
        "voice_sample": "I have a board meeting at 2 PM. I don't care about the cost, just get me there.",
        "tone": "Direct, authoritative, efficiency-focused. Give bottom-line recommendations first.",
        "opportunity_cost": "Extremely high time value. A delayed flight means lost deals, missed board meetings, and wasted billable hours. Will gladly spend money to save time.",
        "customer_behavior": "Highly loyal to airline alliances for status. Uses priority lanes. Delegates tasks. Low tolerance for friction or poor customer service.",
        "flight_preferences": "Early morning departures (first flight out to avoid cascading delays), direct flights only, legacy carriers (Delta, United, AA), premium economy or domestic first class.",
        "coping_style": "Productivity Protection. Find the nearest Lounge. Get on Wi-Fi immediately. Re-book simultaneously on another airline.",
        "insurance": {
            "name": "Corporate Shield Elite",
            "focus": "Time & Financial Assurance",
            "payout": "100% Instant Refund + $1,000 Incidental Coverage for walk-up competitor fares.",
            "recommendation_logic": "Pitch this as 'protecting their hourly rate' rather than saving money."
        }
    },

    "student": {
        "label": "🎒 Student / Young Traveler",
        "voice_sample": "I have like $20 left for food. Can I sleep in the terminal?",
        "tone": "Casual, empathetic, frugal, resourceful. Give cost-saving hacks.",
        "opportunity_cost": "High monetary value, low time value. Losing $100 on a rebooking fee is a disaster; waiting 6 extra hours is just a minor annoyance.",
        "customer_behavior": "Highly flexible. Travels with just a backpack to avoid fees. Actively hunts for compensation, vouchers, and free airport food.",
        "flight_preferences": "Red-eye flights, budget carriers (Spirit, Frontier, Southwest), flights with long but cheap layovers.",
        "coping_style": "Survival Mode. Locate sleeping spots. Fill water bottles. Download movies on free Wi-Fi.",
        "insurance": {
            "name": "Backpacker Delay-Pay",
            "focus": "Food & Hostel Cover",
            "payout": "$50 instant cash for meals/hostels directly to Venmo/Zelle.",
            "recommendation_logic": "Pitch this as 'guaranteed meal money' so they don't starve during a delay."
        }
    },

    "parent": {
        "label": "🧸 Family / Parent",
        "voice_sample": "I have two toddlers and we are running out of diapers. I cannot do a 4-hour layover.",
        "tone": "Empathetic, practical, reassuring. Use 'We got this' energy. Focus on logistics and child containment.",
        "opportunity_cost": "Sanity and routine. Delays mean child meltdowns, disrupted sleep schedules, and running out of essential supplies.",
        "customer_behavior": "Highly planned but easily stressed by unpredictability. Carries heavy gear (strollers, car seats). Values convenience and proximity over minor cost savings.",
        "flight_preferences": "Mid-day flights (avoids early wake-ups and late bedtimes), direct flights to avoid stroller transfers, airlines with strong family boarding policies (like Southwest).",
        "coping_style": "Chaos Containment. Find the Family Bathroom, locate play areas, or find empty gates to let kids run off energy.",
        "insurance": {
            "name": "Family Harmony Flex",
            "focus": "Sanity Protection",
            "payout": "Reimburses airport hotel day-rates, diapers, and immediate food delivery.",
            "recommendation_logic": "Pitch this as a 'meltdown prevention fund' to buy private space if delayed."
        }
    },

    "retiree": {
        "label": "👴 Retiree / Senior Traveler",
        "voice_sample": "My knees can't handle sitting on these hard chairs for three hours.",
        "tone": "Respectful, patient, clear. No jargon. Focus on physical comfort and step-by-step guidance.",
        "opportunity_cost": "Physical comfort and peace of mind. High stress from technology failures or physical exhaustion.",
        "customer_behavior": "Arrives 3 hours early. Prefers human interaction over apps. Needs clear, printed instructions. Values comfort and safety above all.",
        "flight_preferences": "Mid-morning to early-afternoon flights, direct flights, legacy carriers known for good gate-agent customer service.",
        "coping_style": "Comfort First. Request wheelchair assistance for priority seating. Find a quiet corner away from the main concourse.",
        "insurance": {
            "name": "Silver Comfort Guard",
            "focus": "Health & Comfort",
            "payout": "Lounge access included automatically on 2+ hour delays + Medical evacuation.",
            "recommendation_logic": "Pitch this as 'guaranteed access to a comfortable chair and a human concierge' via a 24/7 phone number."
        }
    },

    "tourist": {
        "label": "📸 Tourist / Vacationer",
        "voice_sample": "We're going to miss our dinner reservation in Rome! This is supposed to be fun.",
        "tone": "Upbeat, adventurous, but helpful. Focus on salvaging the experience.",
        "opportunity_cost": "Lost vacation time and missed prepaid reservations (hotels, tours, dinners).",
        "customer_behavior": "Excited but easily flustered by logistics. Often travels with checked bags. Relies heavily on reviews and itineraries.",
        "flight_preferences": "Flights arriving mid-day to maximize hotel check-in time, package-deal flights, flexible airlines.",
        "coping_style": "Experience Salvage. Research airport attractions, duty-free shopping, or nearby mini-excursions if the delay is massive.",
        "insurance": {
            "name": "Vacation Saver",
            "focus": "Experience Protection",
            "payout": "Reimburses missed non-refundable tours, prepaid hotels, and event tickets.",
            "recommendation_logic": "Pitch this as 'protecting your hard-earned PTO and prepaid experiences'."
        }
    },

    "digital_nomad": {
        "label": "💻 Digital Nomad / Remote Worker",
        "voice_sample": "I need stable upload speed. I have a Zoom call with a client in 45 minutes.",
        "tone": "Tech-savvy, efficient, focused on connectivity and workspace.",
        "opportunity_cost": "Lost billable hours and missed client meetings. Dead batteries are a crisis.",
        "customer_behavior": "Works from lounges or gates. Highly adaptable as long as there is internet. Loyal to tech-friendly airlines.",
        "flight_preferences": "Airlines with fast, verified satellite Wi-Fi (e.g., Delta free Wi-Fi, JetBlue). Off-peak flights to ensure an empty middle seat for laptop space.",
        "coping_style": "Tech Hunt. Immediately map out the best power outlets and strongest Wi-Fi / 5G signal zones in the terminal.",
        "insurance": {
            "name": "Remote Work Shield",
            "focus": "Tech & Connection",
            "payout": "Pays for premium lounge Wi-Fi access and lost billable hours up to $500.",
            "recommendation_logic": "Pitch this as 'business continuity insurance' for freelancers."
        }
    },

    "explorer": {
        "label": "🧗 Adventure / Explorer",
        "voice_sample": "It's all part of the journey. I can sleep on the floor if I have to.",
        "tone": "Chill, stoic, adventurous. Focus on alternative routes and local flavor.",
        "opportunity_cost": "Missing unique experiences, though they are highly resilient to logistical hiccups.",
        "customer_behavior": "Spontaneous, travels extremely light (carry-on only). Views delays as part of the adventure or an excuse to see a new city.",
        "flight_preferences": "Multi-city layovers (chance to explore a new place), local/regional carriers, open-jaw tickets.",
        "coping_style": "Go with the Flow. Talk to locals. Read a book. See if the airline will re-route them through a totally different cool city.",
        "insurance": {
            "name": "Explorer Hazard Pay",
            "focus": "Gear & Activity",
            "payout": "Covers lost specialized gear (hiking/scuba) and missed expedition transport (ferries/trains).",
            "recommendation_logic": "Pitch this to protect highly specific, expensive adventure gear and remote connections."
        }
    },

    "vip": {
        "label": "💎 VIP / Luxury Traveler",
        "voice_sample": "This is unacceptable. Get me the concierge line. I don't wait in lines.",
        "tone": "Polite but highly sophisticated. White-glove style. Offer premium, frictionless solutions.",
        "opportunity_cost": "Loss of privacy, status, and exclusivity. Any friction or waiting in public lines is unacceptable.",
        "customer_behavior": "Delegates everything to assistants or concierges. Uses private terminals. Expects proactive problem solving before they even ask.",
        "flight_preferences": "First-class only, private jet charters, or commercial flights with exclusive tarmac transfers (e.g., Porsche transfers).",
        "coping_style": "Total Outsourcing. Call concierge immediately and delegate the rebooking process. Retreat to the most exclusive lounge available.",
        "insurance": {
            "name": "Black Card Infinite",
            "focus": "Exclusivity & Frictionless Travel",
            "payout": "Arranges private black-car transfer to destination or charters a private flight if commercial fails.",
            "recommendation_logic": "Don't pitch the cost. Pitch the 'invisible safety net' that guarantees they never wait with the general public."
        }
    },

    "immigrant": {
        "label": "🌍 Immigrant / Expat",
        "voice_sample": "I have 3 checked bags with gifts for my family. I cannot lose them.",
        "tone": "Serious, protective, detail-oriented. Reassure them about baggage and documentation.",
        "opportunity_cost": "Extremely high emotional stakes (seeing family after years). High risk regarding baggage (gifts/essentials) and visa expiration.",
        "customer_behavior": "Carries maximum baggage allowance. Anxious about customs and immigration. Plans trips months in advance.",
        "flight_preferences": "Legacy carriers with generous international baggage allowances. Flights with layovers only in visa-friendly or transit-friendly countries.",
        "coping_style": "Asset Protection. Stay near the gate desk to visually track baggage loading. Double-check all transit visas.",
        "insurance": {
            "name": "Global Roots Cover",
            "focus": "Baggage & Visa Protection",
            "payout": "$2000 per lost bag + coverage for re-booking if a transit visa expires due to delay.",
            "recommendation_logic": "Pitch this as absolute security for the gifts they are bringing home and their immigration status."
        }
    },

    "commuter": {
        "label": "🚆 Commuter / Short-Haul",
        "voice_sample": "I just want to get home for dinner. I do this flight every Tuesday.",
        "tone": "Brisk, experienced, efficient. Skip the pleasantries; give them raw data and fast alternatives.",
        "opportunity_cost": "Lost evening time at home. Disruption of a highly tuned weekly routine.",
        "customer_behavior": "Knows the airport perfectly. Travels with just a briefcase. Boards last, exits first. Has TSA PreCheck and CLEAR.",
        "flight_preferences": "High-frequency routes (e.g., hourly shuttles). Prefers regional airports over major hubs (e.g., DAL instead of DFW, LGA instead of JFK).",
        "coping_style": "Routine Optimization. Immediately calculate if a rental car or train is faster than waiting for the next shuttle flight.",
        "insurance": {
            "name": "Commuter Express",
            "focus": "On-Time Guarantee",
            "payout": "Instantly covers a premium rental car or Amtrak ticket if the flight is delayed > 2 hours.",
            "recommendation_logic": "Pitch this as a 'get home for dinner' guarantee, empowering them to ditch the airline and drive."
        }
    }

}