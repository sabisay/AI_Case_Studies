import { useState, useEffect } from "react";
import { fetchResponse, fetchAvailablePDFs } from "./api";

function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [pdfs, setPdfs] = useState([]);
  const [selectedPdf, setSelectedPdf] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    // Fetch available PDFs when component mounts
    const getPdfs = async () => {
      const result = await fetchAvailablePDFs();
      if (result.pdfs && result.pdfs.length > 0) {
        setPdfs(result.pdfs);
        setSelectedPdf(result.pdfs[0]); // Select first PDF by default
      }
    };

    getPdfs();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;

    setIsLoading(true);
    setResponse("");

    try {
      const result = await fetchResponse(query, selectedPdf);
      setResponse(result.response || "No response received.");
    } catch (error) {
      setResponse(`Error: ${error.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px", maxWidth: "800px", margin: "0 auto", fontFamily: "Arial" }}>
      <h1>RAG Query System</h1>

      <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
        <div style={{ marginBottom: "15px" }}>
          <label htmlFor="pdf-select" style={{ display: "block", marginBottom: "5px", fontWeight: "bold" }}>
            Select PDF:
          </label>
          <select
            id="pdf-select"
            value={selectedPdf}
            onChange={(e) => setSelectedPdf(e.target.value)}
            style={{ width: "100%", padding: "10px", borderRadius: "4px" }}
          >
            {pdfs.length === 0 && <option value="">No PDFs available</option>}
            {pdfs.map((pdf) => (
              <option key={pdf} value={pdf}>
                {pdf}
              </option>
            ))}
          </select>
        </div>

        <div style={{ marginBottom: "15px" }}>
          <label htmlFor="query-input" style={{ display: "block", marginBottom: "5px", fontWeight: "bold" }}>
            Your Question:
          </label>
          <input
            id="query-input"
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="What would you like to know about this document?"
            style={{ width: "100%", padding: "10px", borderRadius: "4px" }}
          />
        </div>

        <button
          type="submit"
          disabled={isLoading || !selectedPdf || !query.trim()}
          style={{
            padding: "10px 20px",
            backgroundColor: "#4CAF50",
            color: "white",
            border: "none",
            borderRadius: "4px",
            cursor: isLoading ? "not-allowed" : "pointer",
            opacity: isLoading || !selectedPdf || !query.trim() ? 0.7 : 1
          }}
        >
          {isLoading ? "Processing..." : "Submit"}
        </button>
      </form>

      <div style={{ marginTop: "30px" }}>
        <h2>Response:</h2>
        {isLoading ? (
          <div style={{ textAlign: "center", padding: "20px" }}>Loading...</div>
        ) : (
          <div
            style={{
              backgroundColor: "black",
              padding: "15px",
              borderRadius: "4px",
              whiteSpace: "pre-wrap",
              minHeight: "100px"
            }}
          >
            {response || "Submit a query to see the response"}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;