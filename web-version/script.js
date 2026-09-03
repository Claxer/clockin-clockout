/* =========================================================
   WORKTIME - EMPLOYEE ATTENDANCE
   Vanilla JavaScript
   ========================================================= */


/* =========================================================
   STORAGE
   ========================================================= */

const STORAGE_KEY = "worktime_attendance";
const EMPLOYEE_KEY = "worktime_employees";
const THEME_KEY = "worktime_theme";
const TARGET_KEY = "worktime_daily_target";


function loadJSON(key, fallback) {
    try {
        const saved = localStorage.getItem(key);

        if (!saved) {
            return fallback;
        }

        return JSON.parse(saved);
    } catch (error) {
        console.error(`Could not load ${key}:`, error);

        return fallback;
    }
}


let attendance = loadJSON(STORAGE_KEY, []);

let employees = loadJSON(EMPLOYEE_KEY, [
    {
        name: "Jose Navoa",
        position: "Administrator",
        department: "Technology"
    },
    {
        name: "Alex Santos",
        position: "Software Engineer",
        department: "Technology"
    },
    {
        name: "Maria Cruz",
        position: "HR Specialist",
        department: "Human Resources"
    }
]);


let dailyTarget = Number(
    localStorage.getItem(TARGET_KEY)
) || 8;


/* =========================================================
   ELEMENTS
   ========================================================= */

const clockElement = document.getElementById("clock");
const clockDate = document.getElementById("clockDate");
const currentDate = document.getElementById("currentDate");

const clockButton = document.getElementById("clockButton");

const attendanceStatus =
    document.getElementById("attendanceStatus");

const statusIcon =
    document.getElementById("statusIcon");

const clockInTime =
    document.getElementById("clockInTime");

const clockOutTime =
    document.getElementById("clockOutTime");

const workingTime =
    document.getElementById("workingTime");

const progressBar =
    document.getElementById("progress");

const todayBadge =
    document.getElementById("todayBadge");

const recentAttendance =
    document.getElementById("recentAttendance");

const attendanceTable =
    document.getElementById("attendanceTable");

const employeeGrid =
    document.getElementById("employeeGrid");

const toastContainer =
    document.getElementById("toastContainer");

const pageTitle =
    document.getElementById("pageTitle");

const themeButton =
    document.getElementById("themeButton");

const darkToggle =
    document.getElementById("darkToggle");

const dailyTargetInput =
    document.getElementById("dailyTarget");

const targetHoursLabel =
    document.getElementById("targetHoursLabel");


/* =========================================================
   DATE / TIME HELPERS
   ========================================================= */


/*
   Uses the user's local date instead of UTC.
   This prevents attendance records from switching
   to the wrong day around midnight.
*/

function getToday() {

    const now = new Date();

    const year = now.getFullYear();

    const month = String(
        now.getMonth() + 1
    ).padStart(2, "0");

    const day = String(
        now.getDate()
    ).padStart(2, "0");

    return `${year}-${month}-${day}`;
}


function formatDate(dateString) {

    if (!dateString) {
        return "—";
    }

    const date =
        new Date(`${dateString}T00:00:00`);

    return date.toLocaleDateString(
        "en-US",
        {
            month: "short",
            day: "2-digit",
            year: "numeric"
        }
    );
}


function formatTime(date) {

    return date.toLocaleTimeString(
        "en-US",
        {
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit"
        }
    );
}


function formatShortTime(dateString) {

    if (!dateString) {
        return "—";
    }

    const date = new Date(dateString);

    if (Number.isNaN(date.getTime())) {
        return "—";
    }

    return date.toLocaleTimeString(
        "en-US",
        {
            hour: "2-digit",
            minute: "2-digit"
        }
    );
}


/* =========================================================
   LIVE CLOCK
   ========================================================= */

function updateClock() {

    const now = new Date();

    const formattedDate =
        now.toLocaleDateString(
            "en-US",
            {
                weekday: "long",
                month: "long",
                day: "numeric",
                year: "numeric"
            }
        );


    clockElement.textContent =
        formatTime(now);

    clockDate.textContent =
        formattedDate;

    currentDate.textContent =
        formattedDate;
}


updateClock();

setInterval(updateClock, 1000);


/* =========================================================
   STORAGE HELPERS
   ========================================================= */

function saveAttendance() {

    localStorage.setItem(
        STORAGE_KEY,
        JSON.stringify(attendance)
    );
}


function saveEmployees() {

    localStorage.setItem(
        EMPLOYEE_KEY,
        JSON.stringify(employees)
    );
}


function saveTarget() {

    localStorage.setItem(
        TARGET_KEY,
        String(dailyTarget)
    );
}


/* =========================================================
   TODAY RECORD
   ========================================================= */

function getTodayRecord() {

    const today = getToday();

    return attendance.find(
        record => record.date === today
    );
}


/* =========================================================
   TOAST
   ========================================================= */

function showToast(message, type = "info") {

    if (!toastContainer) {
        return;
    }

    const toast =
        document.createElement("div");

    toast.className =
        `toast ${type}`;

    toast.textContent =
        message;

    toastContainer.appendChild(toast);


    setTimeout(() => {

        toast.classList.add("hide");

        setTimeout(() => {
            toast.remove();
        }, 250);

    }, 3000);
}


/* =========================================================
   CLOCK IN
   ========================================================= */

function clockIn() {

    const existing =
        getTodayRecord();


    if (existing) {

        if (!existing.clockOut) {

            showToast(
                "You are already clocked in.",
                "info"
            );

        } else {

            showToast(
                "Today's attendance is already completed.",
                "info"
            );

        }

        return;
    }


    const now = new Date();


    /*
       Default schedule:
       Before 9:00 AM = Present
       9:00 AM or later = Late
    */

    const status =
        now.getHours() >= 9
            ? "Late"
            : "Present";


    const record = {

        id: Date.now(),

        date: getToday(),

        clockIn:
            now.toISOString(),

        clockOut: null,

        status: status
    };


    attendance.unshift(record);

    saveAttendance();

    updateUI();


    showToast(
        "Clock-in recorded.",
        "success"
    );
}


/* =========================================================
   CLOCK OUT
   ========================================================= */

function clockOut() {

    const record =
        getTodayRecord();


    if (!record) {

        showToast(
            "You are not clocked in.",
            "error"
        );

        return;
    }


    if (record.clockOut) {

        showToast(
            "You have already clocked out.",
            "info"
        );

        return;
    }


    record.clockOut =
        new Date().toISOString();


    saveAttendance();

    updateUI();


    showToast(
        "Clock-out recorded.",
        "success"
    );
}


/* =========================================================
   CLOCK BUTTON
   ========================================================= */

if (clockButton) {

    clockButton.addEventListener(
        "click",
        () => {

            const record =
                getTodayRecord();


            if (!record) {

                clockIn();

            } else if (!record.clockOut) {

                clockOut();

            } else {

                showToast(
                    "Today's attendance is already complete.",
                    "info"
                );

            }

        }
    );

}


/* =========================================================
   DURATION
   ========================================================= */

function calculateDuration(record) {

    if (!record || !record.clockIn) {
        return 0;
    }


    const start =
        new Date(record.clockIn);


    const end =
        record.clockOut
            ? new Date(record.clockOut)
            : new Date();


    const duration =
        end - start;


    return Math.max(
        duration,
        0
    );
}


function formatDuration(milliseconds) {

    if (!milliseconds || milliseconds <= 0) {
        return "0h 00m";
    }


    const minutes =
        Math.floor(
            milliseconds / 60000
        );


    const hours =
        Math.floor(
            minutes / 60
        );


    const remainingMinutes =
        minutes % 60;


    return `${hours}h ${String(
        remainingMinutes
    ).padStart(2, "0")}m`;
}


/* =========================================================
   TODAY CARD
   ========================================================= */

function updateToday() {

    const record =
        getTodayRecord();


    targetHoursLabel.textContent =
        `${dailyTarget} ${
            dailyTarget === 1
                ? "hour"
                : "hours"
        }`;


    if (!record) {

        attendanceStatus.textContent =
            "Not Clocked In";

        clockInTime.textContent =
            "—";

        clockOutTime.textContent =
            "—";

        workingTime.textContent =
            "0h 00m";

        todayBadge.textContent =
            "NOT STARTED";

        clockButton.textContent =
            "CLOCK IN";

        clockButton.classList.remove(
            "clocked-out"
        );

        statusIcon.textContent =
            "✓";

        progressBar.style.width =
            "0%";

        return;
    }


    clockInTime.textContent =
        formatShortTime(
            record.clockIn
        );


    const duration =
        calculateDuration(record);


    workingTime.textContent =
        formatDuration(duration);


    if (record.clockOut) {

        clockOutTime.textContent =
            formatShortTime(
                record.clockOut
            );

        attendanceStatus.textContent =
            "Shift Completed";

        todayBadge.textContent =
            "COMPLETED";

        clockButton.textContent =
            "SHIFT COMPLETED";

        clockButton.classList.add(
            "clocked-out"
        );

        statusIcon.textContent =
            "✓";

    } else {

        clockOutTime.textContent =
            "—";

        attendanceStatus.textContent =
            "Currently Working";

        todayBadge.textContent =
            "CLOCKED IN";

        clockButton.textContent =
            "CLOCK OUT";

        clockButton.classList.remove(
            "clocked-out"
        );

        statusIcon.textContent =
            "●";
    }


    const hours =
        duration / 3600000;


    const percentage =
        Math.min(
            (hours / dailyTarget) * 100,
            100
        );


    progressBar.style.width =
        `${percentage}%`;
}


/* =========================================================
   RECENT ATTENDANCE
   ========================================================= */

function renderRecentAttendance() {

    recentAttendance.innerHTML = "";


    const recent =
        attendance.slice(0, 7);


    if (recent.length === 0) {

        recentAttendance.innerHTML = `
            <tr>
                <td colspan="6"
                    style="text-align:center;color:var(--color-muted);padding:30px;">
                    No attendance records yet.
                </td>
            </tr>
        `;

        return;
    }


    recent.forEach(record => {

        const date =
            new Date(
                `${record.date}T00:00:00`
            );


        const row =
            document.createElement("tr");


        const statusClass =
            record.status === "Late"
                ? "late"
                : "active";


        row.innerHTML = `

            <td>
                <strong>
                    ${formatDate(record.date)}
                </strong>
            </td>

            <td>
                ${date.toLocaleDateString(
                    "en-US",
                    { weekday: "long" }
                )}
            </td>

            <td>
                ${formatShortTime(
                    record.clockIn
                )}
            </td>

            <td>
                ${formatShortTime(
                    record.clockOut
                )}
            </td>

            <td>
                ${formatDuration(
                    calculateDuration(record)
                )}
            </td>

            <td>
                <span class="status-pill ${statusClass}">
                    ${
                        record.clockOut
                            ? record.status
                            : "Active"
                    }
                </span>
            </td>

        `;


        recentAttendance.appendChild(row);
    });
}


/* =========================================================
   ATTENDANCE TABLE
   ========================================================= */

function renderAttendanceTable(
    list = attendance
) {

    attendanceTable.innerHTML = "";


    if (list.length === 0) {

        attendanceTable.innerHTML = `
            <tr>
                <td colspan="6"
                    style="text-align:center;color:var(--color-muted);padding:30px;">
                    No records found.
                </td>
            </tr>
        `;

        return;
    }


    list.forEach(record => {

        const date =
            new Date(
                `${record.date}T00:00:00`
            );


        const row =
            document.createElement("tr");


        const statusClass =
            record.status === "Late"
                ? "late"
                : "active";


        row.innerHTML = `

            <td>
                <strong>
                    ${formatDate(record.date)}
                </strong>
            </td>

            <td>
                ${date.toLocaleDateString(
                    "en-US",
                    { weekday: "long" }
                )}
            </td>

            <td>
                ${formatShortTime(
                    record.clockIn
                )}
            </td>

            <td>
                ${formatShortTime(
                    record.clockOut
                )}
            </td>

            <td>
                ${formatDuration(
                    calculateDuration(record)
                )}
            </td>

            <td>
                <span class="status-pill ${statusClass}">
                    ${
                        record.clockOut
                            ? record.status
                            : "Active"
                    }
                </span>
            </td>

        `;


        attendanceTable.appendChild(row);
    });
}


/* =========================================================
   STATISTICS
   ========================================================= */

function updateStatistics() {

    const now =
        new Date();


    const month =
        now.getMonth();


    const year =
        now.getFullYear();


    const monthly =
        attendance.filter(record => {

            const date =
                new Date(
                    `${record.date}T00:00:00`
                );


            return (
                date.getMonth() === month &&
                date.getFullYear() === year
            );

        });


    const present =
        monthly.filter(
            record =>
                record.status === "Present" ||
                record.status === "Late"
        ).length;


    const late =
        monthly.filter(
            record =>
                record.status === "Late"
        ).length;


    const totalMilliseconds =
        monthly.reduce(
            (total, record) =>
                total +
                calculateDuration(record),
            0
        );


    const totalHours =
        totalMilliseconds /
        3600000;


    document.getElementById(
        "presentCount"
    ).textContent = present;


    document.getElementById(
        "lateCount"
    ).textContent = late;


    document.getElementById(
        "hoursCount"
    ).textContent =
        `${totalHours.toFixed(1)}h`;


    /*
       Calculate attendance against
       weekdays elapsed in the current month.
    */

    const today =
        now.getDate();


    let workingDays = 0;


    for (
        let day = 1;
        day <= today;
        day++
    ) {

        const date =
            new Date(
                year,
                month,
                day
            );


        const weekday =
            date.getDay();


        if (
            weekday !== 0 &&
            weekday !== 6
        ) {
            workingDays++;
        }
    }


    const attendancePercentage =
        workingDays === 0
            ? 100
            : Math.round(
                (present /
                    workingDays) *
                100
            );


    document.getElementById(
        "attendancePercentage"
    ).textContent =
        `${Math.min(
            100,
            attendancePercentage
        )}%`;
}


/* =========================================================
   EMPLOYEES
   ========================================================= */

function getInitials(name) {

    return name
        .trim()
        .split(/\s+/)
        .map(word => word.charAt(0))
        .slice(0, 2)
        .join("")
        .toUpperCase();
}


function renderEmployees() {

    employeeGrid.innerHTML = "";


    if (employees.length === 0) {

        employeeGrid.innerHTML = `
            <div style="color:var(--color-muted);">
                No employees found.
            </div>
        `;

        return;
    }


    employees.forEach(employee => {

        const card =
            document.createElement("div");


        card.className =
            "employee-card";


        card.innerHTML = `

            <div class="employee-top">

                <div class="employee-avatar">
                    ${getInitials(employee.name)}
                </div>

                <div>

                    <h3>
                        ${escapeHTML(employee.name)}
                    </h3>

                    <p>
                        ${escapeHTML(employee.position)}
                    </p>

                </div>

            </div>


            <div class="employee-details">

                <div>

                    <span>
                        DEPARTMENT
                    </span>

                    <strong>
                        ${escapeHTML(
                            employee.department
                        )}
                    </strong>

                </div>


                <div>

                    <span>
                        STATUS
                    </span>

                    <strong>
                        Active
                    </strong>

                </div>

            </div>

        `;


        employeeGrid.appendChild(card);
    });
}


/* =========================================================
   HTML SAFETY
   ========================================================= */

function escapeHTML(value) {

    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}


/* =========================================================
   NAVIGATION
   ========================================================= */

const navItems =
    document.querySelectorAll(
        ".nav-item"
    );


const pages =
    document.querySelectorAll(
        ".page"
    );


function openPage(pageName) {

    pages.forEach(page => {

        page.classList.toggle(
            "active",
            page.id === pageName
        );

    });


    navItems.forEach(item => {

        item.classList.toggle(
            "active",
            item.dataset.page === pageName
        );

    });


    pageTitle.textContent =
        pageName.charAt(0).toUpperCase() +
        pageName.slice(1);


    if (pageName === "attendance") {
        renderAttendanceTable();
    }


    if (pageName === "employees") {
        renderEmployees();
    }
}


navItems.forEach(button => {

    button.addEventListener(
        "click",
        () => {
            openPage(
                button.dataset.page
            );
        }
    );

});


document
    .querySelectorAll(
        "[data-page]"
    )
    .forEach(element => {

        if (
            !element.classList.contains(
                "nav-item"
            )
        ) {

            element.addEventListener(
                "click",
                () => {
                    openPage(
                        element.dataset.page
                    );
                }
            );

        }

    });


/* =========================================================
   THEME
   ========================================================= */

function applyTheme(theme) {

    const isLight =
        theme === "light";


    document.body.classList.toggle(
        "light",
        isLight
    );


    document.body.classList.toggle(
        "dark",
        !isLight
    );


    darkToggle.checked =
        !isLight;


    localStorage.setItem(
        THEME_KEY,
        theme
    );
}


function toggleTheme() {

    const isCurrentlyLight =
        document.body.classList.contains(
            "light"
        );


    applyTheme(
        isCurrentlyLight
            ? "dark"
            : "light"
    );
}


const savedTheme =
    localStorage.getItem(
        THEME_KEY
    ) || "dark";


applyTheme(savedTheme);


themeButton.addEventListener(
    "click",
    toggleTheme
);


darkToggle.addEventListener(
    "change",
    () => {

        applyTheme(
            darkToggle.checked
                ? "dark"
                : "light"
        );

    }
);


/* =========================================================
   DAILY TARGET
   ========================================================= */

dailyTargetInput.value =
    dailyTarget;


dailyTargetInput.addEventListener(
    "change",
    () => {

        let value =
            Number(
                dailyTargetInput.value
            );


        if (
            Number.isNaN(value) ||
            value < 1
        ) {
            value = 1;
        }


        if (value > 24) {
            value = 24;
        }


        dailyTarget = value;


        dailyTargetInput.value =
            dailyTarget;


        saveTarget();

        updateToday();

        showToast(
            "Daily working target updated.",
            "success"
        );

    }
);


/* =========================================================
   EMPLOYEE MODAL
   ========================================================= */

const employeeModal =
    document.getElementById(
        "employeeModal"
    );


const addEmployeeButton =
    document.getElementById(
        "addEmployeeButton"
    );


const closeModalButton =
    document.getElementById(
        "closeModal"
    );


const employeeForm =
    document.getElementById(
        "employeeForm"
    );


function openEmployeeModal() {

    employeeModal.classList.add(
        "show"
    );

    employeeModal.setAttribute(
        "aria-hidden",
        "false"
    );


    document.getElementById(
        "employeeName"
    ).focus();
}


function closeEmployeeModal() {

    employeeModal.classList.remove(
        "show"
    );

    employeeModal.setAttribute(
        "aria-hidden",
        "true"
    );
}


addEmployeeButton.addEventListener(
    "click",
    openEmployeeModal
);


closeModalButton.addEventListener(
    "click",
    closeEmployeeModal
);


employeeModal.addEventListener(
    "click",
    event => {

        if (
            event.target ===
            employeeModal
        ) {
            closeEmployeeModal();
        }

    }
);


document.addEventListener(
    "keydown",
    event => {

        if (
            event.key === "Escape" &&
            employeeModal.classList.contains(
                "show"
            )
        ) {

            closeEmployeeModal();

        }

    }
);


/* =========================================================
   ADD EMPLOYEE
   ========================================================= */

employeeForm.addEventListener(
    "submit",
    event => {

        event.preventDefault();


        const name =
            document
                .getElementById(
                    "employeeName"
                )
                .value
                .trim();


        const position =
            document
                .getElementById(
                    "employeePosition"
                )
                .value
                .trim();


        const department =
            document
                .getElementById(
                    "employeeDepartment"
                )
                .value
                .trim();


        if (
            !name ||
            !position ||
            !department
        ) {

            showToast(
                "Please complete all fields.",
                "error"
            );

            return;
        }


        employees.push({

            name,

            position,

            department

        });


        saveEmployees();

        renderEmployees();

        employeeForm.reset();

        closeEmployeeModal();


        showToast(
            `${name} added successfully.`,
            "success"
        );

    }
);


/* =========================================================
   FILTERS
   ========================================================= */

const monthFilter =
    document.getElementById(
        "monthFilter"
    );


const statusFilter =
    document.getElementById(
        "statusFilter"
    );


const clearFilter =
    document.getElementById(
        "clearFilter"
    );


function applyFilters() {

    let filtered =
        [...attendance];


    if (monthFilter.value) {

        filtered =
            filtered.filter(
                record =>
                    record.date.startsWith(
                        monthFilter.value
                    )
            );

    }


    if (
        statusFilter.value !==
        "all"
    ) {

        filtered =
            filtered.filter(
                record =>
                    record.status.toLowerCase() ===
                    statusFilter.value
            );

    }


    renderAttendanceTable(
        filtered
    );
}


monthFilter.addEventListener(
    "change",
    applyFilters
);


statusFilter.addEventListener(
    "change",
    applyFilters
);


clearFilter.addEventListener(
    "click",
    () => {

        monthFilter.value = "";

        statusFilter.value =
            "all";

        renderAttendanceTable();

    }
);


/* =========================================================
   EXPORT CSV
   ========================================================= */

const exportButton =
    document.getElementById(
        "exportButton"
    );


exportButton.addEventListener(
    "click",
    exportCSV
);


function csvEscape(value) {

    return `"${String(value)
        .replaceAll('"', '""')}"`;
}


function exportCSV() {

    if (
        attendance.length === 0
    ) {

        showToast(
            "No attendance records to export.",
            "error"
        );

        return;
    }


    let csv =
        "Date,Day,Clock In,Clock Out,Duration,Status\n";


    attendance.forEach(record => {

        const date =
            new Date(
                `${record.date}T00:00:00`
            );


        const day =
            date.toLocaleDateString(
                "en-US",
                {
                    weekday: "long"
                }
            );


        csv += [
            record.date,

            day,

            formatShortTime(
                record.clockIn
            ),

            formatShortTime(
                record.clockOut
            ),

            formatDuration(
                calculateDuration(record)
            ),

            record.status

        ]
        .map(csvEscape)
        .join(",");


        csv += "\n";

    });


    const blob =
        new Blob(
            [csv],
            {
                type:
                    "text/csv;charset=utf-8;"
            }
        );


    const url =
        URL.createObjectURL(
            blob
        );


    const link =
        document.createElement(
            "a"
        );


    link.href = url;

    link.download =
        "attendance-report.csv";


    document.body.appendChild(
        link
    );


    link.click();


    link.remove();


    URL.revokeObjectURL(
        url
    );


    showToast(
        "CSV exported successfully.",
        "success"
    );
}


/* =========================================================
   UI REFRESH
   ========================================================= */

function updateUI() {

    updateToday();

    renderRecentAttendance();

    renderAttendanceTable();

    updateStatistics();

    renderEmployees();
}


updateUI();


/* =========================================================
   LIVE WORKING TIME
   ========================================================= */

setInterval(
    () => {

        const record =
            getTodayRecord();


        if (
            record &&
            !record.clockOut
        ) {

            updateToday();

            updateStatistics();

        }

    },
    30000
);
