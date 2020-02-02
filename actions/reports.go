package actions

import "github.com/gobuffalo/buffalo"

// ReportsShow default implementation.
func ReportsShow(c buffalo.Context) error {
	return c.Render(200, r.HTML("reports/show.html"))
}

// ReportsIndex default implementation.
func ReportsIndex(c buffalo.Context) error {
	return c.Render(200, r.HTML("reports/index.html"))
}

