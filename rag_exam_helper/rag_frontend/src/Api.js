export const fetchResponse = async (query, pdfName) => {
    try {
        const response = await fetch("http://localhost:5000/query", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ query, pdf_name: pdfName }), // Ensure pdf_name is passed correctly
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || "Failed to fetch response");
        }

        return await response.json();
    } catch (error) {
        console.error("Error fetching response:", error);
        return { response: `Error: ${error.message}` };
    }
};

export const fetchAvailablePDFs = async () => {
    try {
        const response = await fetch("http://localhost:5000/pdfs"); // Ensure backend has this route

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || "Failed to fetch PDFs");
        }

        return await response.json();
    } catch (error) {
        console.error("Error fetching PDFs:", error);
        return { pdfs: [] };
    }
};